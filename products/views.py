from django.views import View
from django.http  import JsonResponse

from products.models import *

class ProductListView(View):
    def get(self, request):
        result = [{
                'categoryId':category.id,
                'categoryName':category.category_name,
                'categoryDescription':category.main_description,
                'products':[{
                    'productId' : product.id,
                    'badge':product.badge,
                    'productName':product.name,
                    'size':product.size,
                    'price':product.price,
                    'url':[img.image_url for img in product.productimage_set.all()]
                } for product in Product.objects.filter(category=category.id)]
        } for category in Category.objects.all()]
        
        return JsonResponse({'result':result}, status=200)


class CategoryView(View):
    def get(self, request, category_id):
        category =  Category.objects.get(id=category_id)
        categoryid = Category.objects.get(id=category_id).id

        if categoryid:
            result = []
            res = []
            products = Product.objects.filter(category = categoryid)
            for product in products:
                res.append(
                {
                    'productId' : product.id,
                    'badge':product.badge,
                    'productName':product.name,
                    'size':product.size,
                    'price':product.price,
                    'url':[img.image_url for img in product.productimage_set.all()],
                    'skin_type' : [productskintype.skin_type.skin_type for productskintype in product.skintypes.all()],
                    'feeling' : product.feeling
                })
            # category = Category.objects.get(categoryid)
            result.append({
                'categoryId':categoryid,
                'categoryName':category.category_name,
                'categoryDescription':category.main_description,
                'sub_category_description':category.sub_description,
                'products':res
            })
            return JsonResponse({'result':result}, status=200)