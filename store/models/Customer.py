from django.db import models
from django.contrib.auth.hashers import check_password


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    def __str__(self):
        return self.first_name + " " + self.last_name

    @staticmethod
    def find_customer_by_email(email,password):
        try:
            found =  Customer.objects.get(email=email)
            if check_password(password,found.password) :
                return found
            else:
                return None
        except :
            return None
