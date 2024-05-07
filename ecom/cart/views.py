from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
# Create your views here.


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, "cart_summary.html", {"cart_products" : cart_products, "quantities": quantities })


def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        # lookup product in db
        product = get_object_or_404(Product, id=product_id)
        # save to session
        product_qty = int(request.POST.get('product_qty'))
        cart.add(product=product, quantity=product_qty)
        #get cart qty
        cart_quantity = cart.__len__()
        # return response
        response = JsonResponse({'qty: ': cart_quantity})
        return response


def cart_delete(request):
    pass


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = request.POST.get('product_qty')
        if product_qty:
            # Convert quantity to integer if it's not empty
            product_qty = int(product_qty)
            cart.update(product=product_id, quantity=product_qty)
            response = JsonResponse({'qty': product_qty})
            return response
        else:
            # Handle case where product_qty is empty
            return JsonResponse({'error': 'Product quantity is missing'}, status=400)

