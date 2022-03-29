import jwt

from django.http            import JsonResponse

from django.conf  import settings
from users.models import User

def login_decorator(func):
    def wrapper(self, request):
        try:
            assess_token = request.headers.get('Authorization')
            payload = jwt.decode(assess_token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
            user = User.objects.get(id = payload['user_id'])
            request.user = user
            return func(self, request)

        except jwt.InvalidSignatureError:
            return JsonResponse({'message':'INVALID_TOKEN'}, status=400)

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message':'INVALID_TOKEN'}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_TOKEN'}, status=400)
    return wrapper