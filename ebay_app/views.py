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


def index(request):
    active_products = Product.objects.filter(active=True)
    completed_products = Product.objects.filter(completed=True)
    
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        print("AJAX request received")  # Добавим отладочный вывод

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
                    product.bids_count += 1

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
            if product.forPeople:
                remaining_time = ""
                highest_bid = ""
                # product.bid = product.bid + " €"
            else:
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
        
        print("Active products data:", active_products_data)  # Добавим отладочный вывод

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
    print("COMPLEEEEEEEEEEEETED")

    
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

