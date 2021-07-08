from django.urls import path
from .views import Login,Signup,Home,Cart

urlpatterns = [
    path('', Home.as_view(),name="homepage"),
    path('signup',Signup.as_view(),name="signupscreen"),
    path('login',Login.as_view(),name="loginscreen"),
    path('cart',Cart.as_view(),name="cartscreen")
]