from django.http  import JsonResponse
from django.views import View

from products.models import *

class ProductDetailView(View):
    def get(self, request, product_id):
        try: 
            product = Product.objects.get(id = product_id)
            main_ingredients = Ingredient.objects.filter(productingredient__product_id = product.id, productingredient__major = True)
            skin_type        = SkinType.objects.filter(productskintype__product_id = product_id)
            product_detail = {
                'name'              : product.name,
                'price'             : product.price,
                'size'              : product.size,
                'category'          : product.category.category_name,
                'descriptrion'      : product.description,
                'feeling'           : product.feeling,
                'product_imges'     : [image.url for image in product.productimage_set.all()],
                'main_ingredients'  : [ingredient.name for ingredient in main_ingredients],
                'ingredients'       : [ingredient.name for ingredient in Ingredient.objects.filter(productingredient__product = product_id)],
                'skin_type'         : [type.name for type in skin_type]
            }
            howtouse = product.howtouse
              
            return JsonResponse({'PRODUCT_DETAIL' : product_detail ,'HOW_TO_USE' : howtouse } , status = 200)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'} , status = 404)
        except Product.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_NAME_ERROR'} , status = 404)
            
    
class RecommendedView(View):
    def get(self, request, product_id):
        try:
            category_id         = Product.objects.get(id = product_id).category
            recommend_list = [{
                'name'      : value.name,
                'image'     : [image.url for image in value.productimage_set.all()],
                'skintype'  : [types.skin_type.name for types in value.productskintype_set.all()]
                } for value in Product.objects.filter(category = category_id) if value.id != Product.objects.get(id = product_id).id]
            
            return JsonResponse({'message' : recommend_list }, status = 200)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'} , status = 401)
        except Product.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_NAME_ERROR'} , status = 401)
        


            
