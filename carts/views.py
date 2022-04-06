import json


from django.http import JsonResponse
from django.views import View

from cores.utils import author
from products.models import Product
from carts.models import Cart


class CartView(View):
    @author
    def post(self, request):
        try:
            data       = json.loads(request.body)
            user       = request.user
            product_id = data['product_id']
            carts      = Cart.objects.filter(user_id=user, product_id=product_id)

            if not Product.objects.filter(id=product_id).exists():
                return JsonResponse({'message': 'PRODUCT_DOES_NOT_EXIT'}, status=404)

            if carts.exists():
                for cart in carts:
                    if cart.quantity <= 0 or cart.quantity >= 20:
                        return JsonResponse({'message': 'INVALID_QUANTITY'}, status=400)
                    cart.quantity += 1
                    cart.save()
                    return JsonResponse({'message': 'QUANTITY_CHANGED'}, status=200)

            Cart.objects.create(
                user       = user,
                product_id = product_id,
                quantity   = 1
            )
            return JsonResponse({'message': 'CART_CREATED'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)