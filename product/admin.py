from django.contrib import admin

from product.models import Cart, Customer_info, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Customer_info)