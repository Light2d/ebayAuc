
from django.contrib import admin
from django.urls import path, include  
from ebay_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('', views.index, name='index'),  # Страница входа становится стартовой страницей
    path('product/<int:product_id>/', views.product, name='product'), 
    path('first_payment/', views.first_payment, name='first_payment'),
    path('second_payment/', views.second_payment, name='second_payment'),
    path('set_remaining_time/', views.set_remaining_time, name='set_remaining_time'),
    path('reset_product_parameters/', views.reset_product_parameters, name='reset_product_parameters'),
    path('accounts/', include('allauth.urls')),    
    path('logout/', views.user_login, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)