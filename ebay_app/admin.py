from django.contrib import admin
from .models import Product, ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'active', 'waiting', 'completed', 'remaining_time', 'last_bid', 'highest_bid', 'bid', 'forPeople', 'forBot', 'bids_count']
    list_filter = ['category', 'active', 'completed']
    search_fields = ['name', 'category']

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3  # Количество дополнительных полей для загрузки изображений

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)