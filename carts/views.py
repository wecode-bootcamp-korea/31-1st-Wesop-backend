import json


from django.http import JsonResponse
from django.views import View

from cores.utils import author
from carts.models import Cart


class CartView(View):
    @author
    def post(self, request):
        try:
            data       = json.loads(request.body)
            user       = request.user
            product_id = data['product_id']

            cart, created = Cart.objects.get_or_create(
                user       =user,
                product_id =product_id
            )
            if created:
                return JsonResponse({'message': 'CART_CREATED'}, status=201)
            if cart.quantity > 19:
                return JsonResponse({'message': 'INVALID_QUANTITY'}, status=200)
            cart.quantity += 1
            cart.save()
            return JsonResponse({'message': 'QUANTITY_CHANGED'}, status=200)

        except Cart.DoesNotExist:
            return JsonResponse({'message': 'CART_DOES_NOT_EXIT'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
