import json


from django.http import JsonResponse
from django.views import View

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
    def get(self, request):
        user = request.user
        carts = Cart.objects.filter(user=user)

        if not Cart.objects.filter(user=user).exists():
            return JsonResponse({'message': 'INVALID_USER'}, status=400)

        result = [{
            'userId': user.id,
            'cartId': cart.id,
            'quantity': cart.quantity,
            'productId': cart.product.id,
            'productName': cart.product.name,
            'productSize': cart.product.size,
            'totalPrice': int(cart.quantity * cart.product.price)
        } for cart in carts]
        return JsonResponse({'message': result}, status=200)