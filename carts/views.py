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
    def delete(self, request):
        try:
            cart_id = request.GET.getlist('cart_id')
            user = request.user

            if cart_id==[]:
                return JsonResponse({'message': 'LIST_EMPTY'}, status=400)

            for cart in cart_id:
                if not Cart.objects.filter(id=cart).exists():
                    return JsonResponse({'message': 'CART_DOES_NOT_EXIT'}, status=404)
                Cart.objects.filter(id=cart).delete()
            return JsonResponse({'message': 'CART_DELETED'}, status=200)

        except Cart.DoesNotExist:
            return JsonResponse({'message': 'CART_DOES_NOT_EXIT'}, status=404)
        except ValueError:
            return JsonResponse({'message': 'VALUE_ERROR'}, status=400)