from django.shortcuts import render,redirect
from django.http import HttpResponse
from ..models.Customer import Customer
from django.views import View


class Login(View):

    def get(self,request):
        return render(request, 'login.html')


    def post(self,request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        searchCustomer = Customer.find_customer_by_email(email, password)

        if searchCustomer:
            request.session['customer_id'] = searchCustomer.id
            request.session['email'] = searchCustomer.email
            return redirect('homepage')
        else:
            return HttpResponse("Logged in Error")