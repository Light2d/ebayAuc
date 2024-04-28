from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'active', 'completed', 'remaining_time', 'last_bid', 'highest_bid', 'bid']
    list_filter = ['category', 'active', 'completed']
    search_fields = ['name', 'category']

admin.site.register(Product, ProductAdmin)
