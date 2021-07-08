from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from ..models.Customer import Customer
from django.views import View


class Signup(View):

    def get(self,request) :
        return render(request, 'signup.html')

    def post(self,request):
        f_name = request.POST.get('firstname')
        l_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))

        customer = Customer(first_name=f_name, last_name=l_name,
                            phone=phone, email=email, password=password)

        customer.register()

        return redirect("loginscreen")
