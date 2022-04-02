from django.views import View
from django.http  import JsonResponse

from products.models import *

class ProductListView(View):
    def get(self, request):
        category_id = int(request.GET.get('category_id', 0))
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 0))

        if category_id == 0:
            products = Product.objects.all()[offset:limit]
        else:
            products = Product.objects.filter(category=category_id)[offset:limit]

        result = [{
            'id': product.id,
            'badge':product.badge,  
            'productName':product.name,
            'size':product.size,
            'price':product.price,
            'url':[img.image_url for img in product.productimage_set.all()],
            'category' : {
                'categoryId':product.category.id,
                'categoryName':product.category.category_name,
                'categoryDescription':product.category.main_description
            }
        } for product in products]
        return JsonResponse({'result':result}, status=200)