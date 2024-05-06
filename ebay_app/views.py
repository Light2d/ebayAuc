from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import random
import time
from threading import Timer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import CustomUser

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Создаем пользователя, но не сохраняем в базу данных пока
            raw_password = form.cleaned_data.get('password')
            user.set_password(raw_password)  # Устанавливаем пароль
            user.save()  # Теперь сохраняем пользователя с хэшированным паролем
                
            # Аутентифицируем и входим в систему только что зарегистрированного пользователя
            username = form.cleaned_data.get('username')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Перенаправляем пользователя на главную страницу после успешной регистрации
            else:
                print("User authentication failed")  # Отладочное сообщение
        else:
            print("Form is invalid")  # Отладочное сообщение
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Перенаправить на главную страницу после входа
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def index(request):
    # Ваша логика для главной страницы
    return render(request, 'index.html')
@login_required
def index(request):
    active_products = Product.objects.filter(active=True)
    completed_products = Product.objects.filter(completed=True)
    
    user = request.user
    user_remaining_time = user.user_remaining_time
    user_highest_bid = user.user_highest_bid
    
    
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':

        # Обработка AJAX-запроса для обновления продуктов
        for product in active_products:
            if product.forBot:
                # Уменьшаем время продукта на каждом обновлении
                product.remaining_time -= 1

                # Проверяем, нужно ли обновить ставку для данного товара
                if 1 <= product.remaining_time <= 5:
                    product.highest_bid = product.bid + product.increment

                    product.bid = product.highest_bid + product.increment

                    product.last_bid = generate_random_name()  # Замените на ваш генератор случайных имен
                    product.remaining_time = 20  # ставим время на 20 секунд

                product.save()  # Сохраняем изменения
                
                if product.bid >= product.price:
                    product.waiting = True
                    product.save()
                    
                    # Запускаем таймер для изменения состояния на completed через 10 секунд
                    Timer(3, update_product_state, args=(product.id,)).start()
                    
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
                "waiting": product.waiting,
                "forBot": product.forBot, 
                'user_remaining_time': user_remaining_time,
            })
        
        
        # Возвращаем обновленные данные об активных продуктах
        return JsonResponse({
            'active_products': active_products_data,
            'user_remaining_time': user_remaining_time,
            'user_highest_bid': user_highest_bid,
        })

    # Если это обычный GET-запрос, просто отобразите страницу index
    return render(request, 'index.html', {'active_products': active_products, 'completed_products': completed_products, 'user_remaining_time': user_remaining_time, 'user_highest_bid': user_highest_bid})


def product(request, product_id):
    active_products = Product.objects.filter(active=True)
    product = get_object_or_404(Product, pk=product_id)
    
    user_remaining_time = request.user.user_remaining_time
    
    # Проверяем, является ли запрос AJAX-запросом
    if request.is_ajax():
        # Возвращаем JSON-ответ
        return JsonResponse({
            'user_remaining_time': user_remaining_time,
        })
    else:
        # Рендерим HTML-страницу
        return render(request, 'product.html', {'product': product, 'active_products': active_products, 'user_remaining_time': user_remaining_time})

def update_active_products():
    active_products = Product.objects.filter(active=True)
    for product in active_products:
        if product.forBot:
            # Уменьшаем время продукта на каждом обновлении
            product.remaining_time -= 1

            # Проверяем, нужно ли обновить ставку для данного товара
            if 1 <= product.remaining_time <= 5:
                product.highest_bid = product.bid + product.increment
                product.bid = product.highest_bid + product.increment
                product.last_bid = generate_random_name()  # Замените на ваш генератор случайных имен
                product.remaining_time = 20  # ставим время на 20 секунд

            product.save()  # Сохраняем изменения

            if product.bid >= product.price:
                product.waiting = True
                product.save()

                # Запускаем таймер для изменения состояния на completed через 10 секунд
                Timer(5, update_product_state, args=(product.id,)).start()

                # Запускаем таймер для изменения состояния на active через 15 секунд
                Timer(5, update_product_state2, args=(product.id,)).start()
                
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
    product.remaining_time = 20
    product.bid = 0
    product.save()
  

def generate_random_name():
    # Список возможных имен
    names = ['John', 'Alice', 'Bob', 'Emma', 'James', 'Olivia', 'Michael', 'Sophia', 'William', 'Isabella', 'Liam', 'Ava', 'Noah', 'Mia', 'Ethan', 'Charlotte', 'Mason', 'Amelia', 'Logan', 'Harper', 'Lucas', 'Evelyn', 'Henry', 'Abigail', 'Alexander', 'Emily', 'Jackson', 'Elizabeth', 'Sebastian', 'Sofia']
    
    # Выбираем случайное имя из списка
    random_name = random.choice(names)
    return random_name




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
            user = request.user
            user_remaining_time = user.user_remaining_time
            user.user_remaining_time = user_remaining_time


            # Уменьшаем remaining_time на 1 секунду
            if user_remaining_time > 0:
                user_remaining_time -= 1
                user.user_remaining_time = user_remaining_time
                product.last_bid = "you"
                product.highest_bid = product.increment
                product.bid = product.increment * 2
                product.save()
                user.save()

                for_people = product.forPeople

                # Возвращаем JSON-ответ с успехом, remaining_time и forPeople
                return JsonResponse({'success': True, 'remaining_time': user_remaining_time, 'for_people': for_people})
            else:
                # Если remaining_time достиг нуля, сбрасываем его и last_bid
                user.user_remaining_time = 20
                product.last_bid = ""
                user.save()
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