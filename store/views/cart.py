from django.shortcuts import render
from django.views import View
from ..models.Product import Product

class Cart(View):

    def get(self,request):
        cart = request.session.get('cart')

        if cart is None:
            return render(request, 'cart.html')

        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products': products})

