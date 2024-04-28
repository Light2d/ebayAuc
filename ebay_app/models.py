from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='products/')  # Картинка продукта
    name = models.CharField(max_length=100)  # Название продукта
    description = models.TextField()  # Описание продукта
    category = models.CharField(max_length=50)  # Категория продукта
    active = models.BooleanField(default=True)  # Активный продукт или нет
    completed = models.BooleanField(default=False)  # Завершенный продукт или нет
    remaining_time = models.IntegerField()  # Оставшееся время в минутах
    last_bid = models.CharField(max_length=100, null=True, blank=True)  # Имя последнего ставящего
    highest_bid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Наивысшая ставка
    bid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Ставка

    def __str__(self):
        return self.name