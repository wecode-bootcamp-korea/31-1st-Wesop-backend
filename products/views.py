from django.http  import JsonResponse
from django.views import View

from products.models import *




class ProductDetailView(View):
    def get(self, request, products_name):
        try: 
            # prouduct detail
            item = Product.objects.get(name = products_name)
            item_id = Product.objects.get(name = products_name).id
            product_detail = [{
                'name'              : item.name,
                'price'             : item.price,
                'size'              : item.size,
                'category'          : item.category.category_name,
                'descriptrion'      : item.description,
                'feeling'           : item.feeling,
                'product_imges'     : ProductImage.objects.get(product_id=item_id).image_url,
                'squence'           : [{'squence' : value.ingredient.ingredients} for value in ProductIngredient.objects.filter(product = item_id, squence = 1)],
                'ingredient'        : [{'ingredients' :value.ingredient.ingredients} for value in ProductIngredient.objects.filter(product = item_id)],
                'skin_type'         : [{'skin type' : type.skin_type.skin_type } for type in ProductSkintype.objects.filter(product = item_id )]
            }]
            
            # how to use 
            howtouse = item.howtouse
            
            # recommend
            product_category    = Product.objects.get(name = products_name).category
            Product.objects.filter(category = product_category)
            recommend_list = [{
                'name'      : item.name,
                'image'     : ProductImage.objects.get(product = item.id).image_url,
                'skintype'  : ProductSkintype.objects.get(product = item.id).skin_type.skin_type,
                } for item in Product.objects.filter(category = product_category) if item != Product.objects.get(name= products_name)]
            return JsonResponse({'PRODUCT_DETAIL' : product_detail ,'HOW_TO_USE' : howtouse , 'RECOMMEND' : recommend_list} , status = 200)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'} , status = 404)
        except Product.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_NAME_ERROR'} , status = 404)
            
    
# class HowToUseView(View):
#     def get(self, request , products_name):
#         try:
#             product  = Product.objects.get(name = products_name)
#             howtouse = product.howtouse
#             return JsonResponse({'message' : howtouse} , status = 200)
#         except KeyError:
#             return JsonResponse({'message' : 'KEY_ERROR'} , status = 401)
#         except Product.DoesNotExist:
#             return JsonResponse({'message' : 'PRODUCT_NAME_ERROR'} , status = 404)
        
# class RecommendedView(View):
#     def get(self, request, products_name):
#         try:
#             product_category    = Product.objects.get(name = products_name).category
#             Product.objects.filter(category = product_category)
#             recommend_list = [{
#                 'name'      : item.name,
#                 'image'     : ProductImage.objects.get(product = item.id).image_url,
#                 'skintype'  : ProductSkintype.objects.get(product = item.id).skin_type.skin_type,
#                 } for item in Product.objects.filter(category = product_category) if item != Product.objects.get(name= products_name)]
#             return JsonResponse({'message' : recommend_list }, status = 200)
#         except KeyError:
#             return JsonResponse({'message' : 'KEY_ERROR'} , status = 401)
#         except Product.DoesNotExist:
#             return JsonResponse({'message' : 'PRODUCT_NAME_ERROR'} , status = 401)
        


            
