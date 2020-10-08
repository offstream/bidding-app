from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'expiry_date')
    search_fields = ('name', 'user')


admin.site.register(Product, ProductAdmin)
