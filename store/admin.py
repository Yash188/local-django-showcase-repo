from django.contrib import admin
from .models.Product import Product
from .models.Category import Category
from .models.Customer import Customer


class ProductModelAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ["name","price","category","image"]

    def download_csv(self,request,queryset):
        import csv
        from django.http import HttpResponse
        from io import StringIO

        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["Product Name","Price","Category"])

        for s in queryset:
            writer.writerow([s.name,s.price,s.category])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=products.csv'
        return response


    download_csv.short_description = "Download CSV file for selected stats."


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name"]


class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","phone","email"]


# Register your models here.
admin.site.register(Product,ProductModelAdmin)
admin.site.register(Category,CategoryModelAdmin)
admin.site.register(Customer,CustomerModelAdmin)