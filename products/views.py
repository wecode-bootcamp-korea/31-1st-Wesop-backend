
from django.http  import JsonResponse
from django.views import View

from products.models import *

class RecommendedView(View):
    def get(self, request, product_id):
        try:
            category_id         = Product.objects.get(id = product_id).category
            recommend_list = [{
                'name'      : product.name,
                'image'     : [image.url for image in product.productimage_set.all()],
                'skintype'  : [types.skin_type.name for types in product.productskintype_set.all()]
                } for product in Product.objects.filter(category = category_id).exclude(id=product_id)]

            return JsonResponse({'result' : [ recommend_list ] }, status = 200)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'} , status = 401)
        except Product.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_NAME_ERROR'} , status = 401)