from django.views import View
from django.http  import JsonResponse
from django.db.models import Q

from products.models import *

class ProductListView(View):
    def get(self, request):
        category_id = request.GET.get('category_id', None)
        offset      = int(request.GET.get('offset', 0))
        limit       = int(request.GET.get('limit', 100))
        ingredient  = request.GET.getlist('ingredient', None)
        skintype   = request.GET.getlist('skintype', None)
        badge       = request.GET.getlist('badge', None)
        feeling     = request.GET.get('feeling', None)
        
        q = Q()

        if category_id:
            q &= Q(category__id=category_id)

        if badge:
            q &= Q(badge__in=badge)
        
        if ingredient:
            q &= Q(productingredient__ingredient__id__in=ingredient)
        
        if skintype:
            q &= Q(skintypes__skin_type__id__in=skintype)
        
        if feeling:
            q &= Q(productfeelings__feeling__id__in=feeling)
        
        products = Product.objects.filter(q)[offset:limit]

        result = [{
            'id'         : product.id,
            'badge'      : product.badge,
            'productName': product.name,
            'size'       : product.size,
            'price'      : product.price,
            'feeling'    : [feeling.feeling.name for feeling in product.productfeelings_set.all()],
            'ingredient' : [item.ingredient.name for item in product.productingredient_set.all()],
            'skin_type'  : [productskintype.skin_type.name for productskintype in product.productskintype_set.all()],
            'url'        : [img.url for img in product.productimage_set.all()],
            'category'   : {
                'categoryId'         : product.category.id,
                'categoryName'       : product.category.category_name,
                'categoryDescription': product.category.main_description,
                'categorySubDescription': product.category.sub_description
            }
        } for product in products]
        return JsonResponse({'result':result}, status=200)