from django.db import models
from .Category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default="", null=True, blank=True)
    image = models.ImageField(upload_to="uploads/products/")

    def __str__(self):
        return self.name

    @staticmethod
    def getAllProducts():
        return Product.objects.all()

    @staticmethod
    def getProductbyCategoryId(category_id):
        if category_id :
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)