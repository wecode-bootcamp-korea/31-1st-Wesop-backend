from django.http import JsonResponse
from django.views    import View
import json

from products.models import *
from users.models    import *

class ProductReview(View):
    def post(self, request, product_id, user_id):
        try:
            data = json.loads(request.body)
            content = data['content']
            product = Product.objects.get(product = product_id)
            user    = User.objects.get(id = user_id)
            
            post_review = ReviewImage.objects.create(
                user    = user.id,
                product = product.id, 
                content = content
            )
            return JsonResponse({'result' : post_review } , status =200) 
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'} , status = 401)
        except Product.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_DOES_NOT_EXIST'} , status = 400)
        