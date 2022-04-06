import json
import bcrypt
import jwt

from django.conf import settings
from django.http import JsonResponse
from django.forms import ValidationError

from datetime import datetime, timedelta
from cores.validations import validate_email, validate_password
from .models import User


def check_email(request):
    try:
        if not request.method == 'POST':
            return JsonResponse({'message' : 'INVALID_METHOD'}, status=405)

        data  = json.loads(request.body)
        email = data['email']

        validate_email(email)

        is_exit = User.objects.filter(email=email).exists()
        return JsonResponse({'message' : is_exit}, status=200)

    except ValidationError:
        return JsonResponse({'message' : 'VALIDATION_ERROR'}, status=400)
    except KeyError:
        return JsonResponse({'message' : 'KEY_ERROR'}, status=400)


def sign_up(request):
    try:
        if not request.method == 'POST':
            return JsonResponse({'message' : 'INVALID_METHOD'}, status=405)

        data       = json.loads(request.body)
        email      = data['email']
        password   = data['password']
        last_name  = data['last_name']
        first_name = data['first_name']

        validate_email(email)
        validate_password(password)

        if User.objects.filter(email = email).exists():
            return JsonResponse({'message' : 'ALREADY_EXIST_EMAIL'}, status=400)

        user = User.objects.create(
            email      = email,
            password   = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            last_name  = last_name,
            first_name = first_name
        )

        token = jwt.encode({'id': user.id, 'exp': datetime.utcnow() + timedelta(days=1)},
                           settings.SECRET_KEY,
                           settings.ALGORITHM)

        return JsonResponse({
                'message': 'SUCCESS',
                'token': token,
                'firstName': user.first_name,
                'lastName': user.last_name,
                'email': user.email,
                'userId': user.id
            }, status=201)

    except ValidationError:
        return JsonResponse({'message' : 'VALIDATION_ERROR'}, status=400)
    except KeyError:
        return JsonResponse({'message' : 'KEY_ERROR'}, status=400)


def log_in(request):
    try:
        if not request.method == 'POST':
            return JsonResponse({'message' : 'INVALID_METHOD'}, status=405)
            
        data     = json.loads(request.body)
        email    = data['email']
        password = data['password']
        user     = User.objects.get(email=email)

        validate_email(email)
        validate_password(password)

        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return JsonResponse({'message' : 'INVALID_PASSWORD'}, status=401)

        token = jwt.encode({'id': user.id, 'exp': datetime.utcnow() + timedelta(days=1)},
                           settings.SECRET_KEY,
                           settings.ALGORITHM)

        return JsonResponse({
                'message': 'SUCCESS',
                'token': token,
                'firstName': user.first_name,
                'lastName': user.last_name,
                'email': user.email,
                'userId': user.id
            }, status=200)

    except User.DoesNotExist:
        return JsonResponse({'message' : 'USER_DOES_NOT_EXIST'}, status=404)
    except ValidationError:
        return JsonResponse({'message' : 'VALIDATION_ERROR'}, status=400)
    except KeyError:
        return JsonResponse({'message' : 'KEY_ERROR'}, status=400)