from http.client import HTTPResponse
from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import random
import time
from threading import Timer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def index(request):
    active_products = Product.objects.filter(active=True)
    completed_products = Product.objects.filter(completed=True)
    
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':

        # Обработка AJAX-запроса для обновления продуктов
        for product in active_products:
            if product.forBot:
                # Уменьшаем время продукта на каждом обновлении
                product.remaining_time -= 1

                # Проверяем, нужно ли обновить ставку для данного товара
                if 5 <= product.remaining_time <= 15:
                    product.bid += product.increment
                    product.last_bid = generate_random_name()  # Замените на ваш генератор случайных имен
                    product.remaining_time = 20  # ставим время на 20 секунд

                product.save()  # Сохраняем изменения
                
                if product.bid >= product.highest_bid:
                    product.waiting = True
                    product.save()
                    
                    # Запускаем таймер для изменения состояния на completed через 10 секунд
                    Timer(5, update_product_state, args=(product.id,)).start()
                    
                    # Запускаем таймер для изменения состояния на active через 15 секунд
                    Timer(5, update_product_state2, args=(product.id,)).start()
                    
        # Получаем обновленные данные об активных продуктах
        active_products_data = []
        for product in active_products:
           
            remaining_time = product.remaining_time
            highest_bid = product.highest_bid
            
            active_products_data.append({
                "id": product.id,
                "remaining_time": remaining_time,
                "last_bid": product.last_bid,
                "highest_bid": highest_bid,
                "bid": product.bid,
                "waiting": product.waiting 
            })
        
        
        # Возвращаем обновленные данные об активных продуктах
        return JsonResponse({
            'active_products': active_products_data,
        })

    # Если это обычный GET-запрос, просто отобразите страницу index
    return render(request, 'index.html', {'active_products': active_products, 'completed_products': completed_products})


def update_product_state(product_id):
    product = Product.objects.get(id=product_id)
    product.completed = True
    product.active = False
    product.waiting = False
    product.save()

    
def update_product_state2(product_id):
    time.sleep(5)  # Ждем 5 секунд
    product = Product.objects.get(id=product_id)
    product.completed = False
    product.active = True
    product.bid = product.initial_bid
    product.save()

def generate_random_name():
    # Список возможных имен
    names = ['John', 'Alice', 'Bob', 'Emma', 'James', 'Olivia', 'Michael', 'Sophia', 'William', 'Isabella']
    
    # Выбираем случайное имя из списка
    random_name = random.choice(names)
    return random_name



def product(request, product_id):
    active_products = Product.objects.filter(active=True)
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product.html', {'product': product, 'active_products': active_products})

def second_payment(request):
    return render(request, 'second_payment.html')

def first_payment(request):
    return render(request, 'first_payment.html')


@csrf_exempt
def set_remaining_time(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
            remaining_time = product.remaining_time

            # Уменьшаем remaining_time на 1 секунду
            if remaining_time > 0:
                remaining_time -= 1
                product.remaining_time = remaining_time
                # product.highest_bid = product.bid
                product.last_bid = "you"
                product.save()

                for_people = product.forPeople

                # Возвращаем JSON-ответ с успехом, remaining_time и forPeople
                return JsonResponse({'success': True, 'remaining_time': remaining_time, 'for_people': for_people})
            else:
                # Если remaining_time достиг нуля, сбрасываем его и last_bid
                product.remaining_time = 20
                product.last_bid = ""
                product.save()
                return JsonResponse({'success': True, 'remaining_time': 20, 'for_people': product.forPeople})
        except Product.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'})
    
@csrf_exempt
def reset_product_parameters(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
            product.remaining_time = 20
            product.last_bid = "-"
            product.save()
            return JsonResponse({'success': True})
        except Product.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'})