import json

from django.views import View
from django.http  import JsonResponse

from products.models import *

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        result = []

        for product in products:
            result.append({
                'category_id':Category.objects.get(id=product.category.id).id,
                'category_name':Category.objects.get(id=product.category.id).category_name,
                'category_description':ProductDescription.objects.get(id=product.category.id).list_description,
                'products':[
                    {
                        'badge':product.badge,
                        'product_name':product.name,
                        'size':product.size,
                        'price':product.price,
                        'product_url':[img.image_url for img in ProductImage.objects.all()]
                    }
                ]
            })
        return JsonResponse({'result':result}, status=200)
