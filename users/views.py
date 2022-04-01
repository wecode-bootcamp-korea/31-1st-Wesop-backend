import json


from django.conf import settings
from django.http import JsonResponse
from django.forms import ValidationError
import bcrypt
import jwt

from cores.validations import validate_email, validate_password
from .models import *


def check_email(request):
    try:
        if not request.method == 'POST':
            return JsonResponse({"message" : "INVALID_METHOD"}, status=405) 

        data  = json.loads(request.body)
        email = data['email']

        validate_email(email)

        IS_EXITS = User.objects.filter(email = email).exists()
        return JsonResponse({'message' : IS_EXITS}, status = 200)

    except ValidationError:
            return JsonResponse({'message' : 'VALIDATION_ERROR'}, status = 400)
    except KeyError:
        return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

def sign_up(request):
        try:
            if not request.method == 'POST':
                return JsonResponse({"message" : "INVALID_METHOD"}, status=405) 

            data       = json.loads(request.body)
            email      = data['email']
            password   = data['password']
            last_name  = data['last_name']
            first_name = data['first_name']

            validate_email(email)
            validate_password(password)

            User.objects.create(
                email      = email,
                password   = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                last_name  = last_name,
                first_name = first_name
            )

            user  = User.objects.get(email = email)
            token = jwt.encode({"id" :user.id}, settings.SECRET_KEY, settings.ALGORITHM)

            return JsonResponse({'message' : 'SUCCESS', 'token' : token}, status = 201)

        except ValidationError:
            return JsonResponse({'message' : 'VALIDATION_ERROR'}, status = 400)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

def log_in(request):
    try:
        if not request.method == 'POST':
            return JsonResponse({"message" : "INVALID_METHOD"}, status=405) 
            
        data     = json.loads(request.body)
        email    = data['email']
        password = data['password']

        validate_email(email)
        validate_password(password)

        user  = User.objects.get(email = email)
        token = jwt.encode({"id" :user.id}, settings.SECRET_KEY, settings.ALGORITHM)

        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status=401)

        return JsonResponse({"message" : "SUCCESS","token" : token}, status=200)

    except User.DoesNotExist:
        return JsonResponse({"message" : "USER_DOES_NOT_EXIST"}, status=404)
    except ValidationError:
        return JsonResponse({'message' : 'VALIDATION_ERROR'}, status = 400)
    except KeyError:
        return JsonResponse({"message" : "KEY_ERROR"}, status=400)
