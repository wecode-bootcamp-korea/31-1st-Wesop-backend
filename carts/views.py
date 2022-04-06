import json


from django.http import JsonResponse
from django.views import View
from products.models import Product

from cores.utils import author
from carts.models import Cart


class CartView(View):
    @author
    def post(self, request):
        try:
            data = json.loads(request.body)

            cart, created = Cart.objects.get_or_create(
                user       = request.user,
                product_id = data['product_id']
            )
            if not created and cart.quantity < 20:
                cart.quantity += 1
                cart.save()
            else:
                return JsonResponse({'message': 'INVALID_QUANTITY'}, status=200)

            return JsonResponse({'message': 'CART_CREATED'}, status=201)

        except Cart.DoesNotExist:
            return JsonResponse({'message': 'CART_DOES_NOT_EXIT'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

    @author
    def patch(self, request):
        try:
            data       = json.loads(request.body)
            user       = request.user
            cart_id    = data['cart_id']
            quantity   = data['quantity']

            if quantity <= 0 or quantity >= 21:
                return JsonResponse({'message': 'INVALID_QUANTITY'}, status=400)

            if not Cart.objects.filter(id=cart_id, user_id=user).exists():
                return JsonResponse({'message': 'CART_DOES_NOT_EXIT'}, status=404)
            cart          = Cart.objects.get(user_id=user, id=cart_id)
            cart.quantity = quantity
            cart.save()
            return JsonResponse({'message': 'QUANTITY_CHANGED'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
