from django.contrib import admin
from .models import Product, ProductImage, ProductAttribute

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3  # Количество дополнительных полей для загрузки изображений

class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1  # Количество дополнительных полей для добавления атрибутов

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'active', 'waiting', 'completed', 'remaining_time', 'last_bid', 'highest_bid', 'bid', 'forPeople', 'forBot']
    list_filter = ['category', 'active', 'completed']
    search_fields = ['name', 'category']
    inlines = [ProductImageInline, ProductAttributeInline]

admin.site.register(Product, ProductAdmin)
