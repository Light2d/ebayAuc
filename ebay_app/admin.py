from django.contrib import admin
from .models import CustomUser, Product, ProductImage, ProductAttribute

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3  # Количество дополнительных полей для загрузки изображений

class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1  # Количество дополнительных полей для добавления атрибутов

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'active', 'waiting', 'completed', 'remaining_time', 'last_bid', 'highest_bid', 'bid', 'forPeople', 'forBot']
    list_filter = ['active',]
    search_fields = ['name',]
    inlines = [ProductImageInline, ProductAttributeInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(CustomUser)
