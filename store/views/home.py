from django.shortcuts import render,redirect
from ..models.Category import Category
from ..models.Product import Product
from django.views import View

class Home(View):

    def post(self,request):

        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        product = request.POST.get('product')


        if cart :
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity-1 <= 0:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1;
                else:
                    cart[product] = quantity + 1;
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('homepage')

    def get(self,request):
        products = None
        category = Category.getAllCategory()
        product_query = request.GET.get('category')
        if product_query:
            products = Product.getProductbyCategoryId(product_query)
        else:
            products = Product.getAllProducts()

        cart = request.session.get('cart')
        print('Cart',cart)

        #if not cart is None:
            #del request.session['cart']

        return render(request, 'index.html', {'products': products, 'categories': category})

