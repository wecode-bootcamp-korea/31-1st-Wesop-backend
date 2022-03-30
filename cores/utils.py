import jwt

from django.conf import settings
from ..orders.models import User

from django.http import JsonResponse

def logindeco(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            assess_token = request.headers.get('Authorization')
            payload = jwt.decode(assess_token, settings.SECRET_KEY, settings.ALGORITHM)
            user = User.objects.get(id = payload['user_id'])
            request.user = user
            return func(self, request, *args, **kwargs)

        except jwt.InvalidSignatureError:
            return JsonResponse({'message':'INVALID_SIGNATURE_ERROR'}, status=400)

        except jwt.exceptions.DecodeError:                                     
            return JsonResponse({'message' : 'DECODE_ERROR' }, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({'message' : 'USER_DOES_NOT_EXIST_ERROR'}, status=400)

    return wrapper
