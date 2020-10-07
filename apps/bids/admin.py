from django.contrib import admin
from .models import Bid


class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'is_accepted', 'created_at')
    search_fields = ('user', 'product')


admin.site.register(Bid, ProductAdmin)
