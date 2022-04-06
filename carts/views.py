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

    @author
    def get(self, request):
        user  = request.user
        carts = Cart.objects.filter(user=user)

        if not Cart.objects.filter(user=user).exists():
            return JsonResponse({'message': 'INVALID_USER'}, status=400)

        result = [{
            'userId'     : user.id,
            'cartId'     : cart.id,
            'quantity'   : cart.quantity,
            'productId'  : cart.product.id,
            'productName': cart.product.name,
            'productSize': cart.product.size,
            'totalPrice' : int(cart.quantity * cart.product.price)
            }for cart in carts]

        return JsonResponse({'message': result}, status=200)

    @author
    def delete(self, request):
        try:
            cart_id = request.GET.getlist('cart_id')
            user       = request.user

            if cart_id == []:
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

    @author
    def patch(self, request):
        try:
            data       = json.loads(request.body)
            user       = request.user
            product_id = data['product_id']
            quantity   = data['quantity']
            product    = Product.objects.get(id=product_id)

            if quantity <= 0 or quantity >= 21:
                return JsonResponse({'message': 'INVALID_QUANTITY'}, status=400)

            if not Cart.objects.filter(product_id=product_id, user_id=user).exists():
                return JsonResponse({'message': 'PRODUCT_DOES_NOT_EXIT'}, status=400)

            if Cart.objects.filter(product_id=product).exists():
                    cart          = Cart.objects.get(user=user, product_id=product)
                    cart.quantity = quantity
                    cart.save()
                    return JsonResponse({'message': 'QUANTITY_CHANGED'}, status=201)
            return JsonResponse({'message': 'NO_PRODUCT_IN_CART'}, status=400)

        except Product.DoesNotExist:
            return JsonResponse({'message': "INVALID_PRODUCT"})
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
