import json

from django.http     import JsonResponse
from django.views    import View

from products.models import Product , Review
from users.models    import User

class ProductReview(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            content = data['content']
            
            product = Product.objects.get(id = request.GET.get('product_id') )
            user    = User.objects.get(id = request.GET.get('user_id'))
            
            Review.objects.create(  
                user    = user,
                product = product, 
                content = content
            )
             
            return JsonResponse({'message' : 'SUCCESS'} , status = 201) 
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'} , status = 400)
        except Product.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_DOES_NOT_EXIST'} , status = 404)
        
    def get(self, request):
        try:
            product_reviews =Review.objects.filter(product_id = request.GET.get('product_id'))
            if product_reviews.exists():
                product_review_list = [{
                    'review_id' : review.id,
                    'user'      : review.user.email,
                    'content'   : review.content
                    } for review in product_reviews]
            return JsonResponse({'message' : product_review_list} , status =200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'} , status = 400)
        except Product.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_DOES_NOT_EXIST'} , status = 400)
        

    def delete(self, request):
        try:
            data = json.loads(request.body)
            user_id    = request.GET.get('user_id')
            product_id = request.GET.get('product_id')
            
            review  = Review.objects.get(id=data['review_id'])
                
            if not Review.objects.filter(user_id = user_id , product_id = product_id).exists():
                return JsonResponse({'message' : 'REVIEW_DOES_NOT_EXIST'} , status = 404)
            
            review.delete()
                
            return JsonResponse({'message' : 'SUCCESS'} , status = 200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'} , status = 400)
        except Review.DoesNotExist:
            return JsonResponse({'message' : 'REVIEW_DOES_NOT_EXIST'} , status = 400)
        
        
        
        

        