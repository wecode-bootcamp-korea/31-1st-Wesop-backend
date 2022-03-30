import json
import bcrypt
import jwt

from django.conf import settings
from django.http import JsonResponse
from django.forms import ValidationError

from cores.validations import email_validation, password_validation
from .models import *


def CheckEmail(request):
    try:
        if request.method == 'POST':
            data  = json.loads(request.body)
            email = data['email']

            email_validation(email)

            if not User.objects.filter(email = email).exists():
                return JsonResponse({'message' : 'FALSE'}, status = 200)
            return JsonResponse({'message' : 'TRUE'}, status = 200)

    except KeyError:
        return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

def SignUp(request):
        try:
            if request.method == 'POST':
                data       = json.loads(request.body)
                email      = data['email']
                password   = data['password']
                last_name  = data['last_name']
                first_name = data['first_name']

            password_validation(password)

            User.objects.create(
                email = email,
                password   = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                last_name  = last_name,
                first_name = first_name
            )
            return JsonResponse({'message' : 'SUCCESS'}, status = 201)

        except ValidationError:
            return JsonResponse({'message' : 'VALIDATION_ERROR'}, status = 400)
        except:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

def Login(request):
    try:
        if request.method == 'POST':
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            email_validation(email)
            password_validation(password)

            user     = User.objects.get(email = email)
            token    = jwt.encode({"id" :user.id}, settings.SECRET_KEY, settings.ALGORITHM)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                    return JsonResponse({"message" : "INVALID_PASSWORD"}, status=401)
            return JsonResponse({"message" : "SUCCESS","token" : token}, status=200)

    except User.DoesNotExist:
        return JsonResponse({"message" : "USER_DOES_NOT_EXIST"}, status=401)
    except ValidationError:
        return JsonResponse({'message' : 'VALIDATION_ERROR'}, status = 400)
    except KeyError:
        return JsonResponse({"message" : "KEY_ERROR"}, status=400)
