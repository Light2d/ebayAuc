
from django.contrib import admin
from django.urls import path
from ebay_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('product/<int:product_id>/', views.product, name='product'),  # Обновленный путь
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
