from django.contrib import admin
from .models import Product  # Import the Product model

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('nombre', 'descripcion', 'precio', 'available', 'photo')
    search_fields = ('nombre', 'descripcion')

admin.site.register(Product, ProductAdmin)    