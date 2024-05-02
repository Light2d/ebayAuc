from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    condition = models.TextField()
    category = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    waiting = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    remaining_time = models.IntegerField(null=True)
    last_bid = models.CharField(max_length=100, null=True, blank=True)
    highest_bid = models.IntegerField(default=0)
    increment = models.IntegerField(default=0)
    initial_bid = models.IntegerField(default=0)
    bid = models.IntegerField(default=0)
    forPeople = models.BooleanField(default=False)
    forBot = models.BooleanField(default=False)

    
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product.name + ' Image'

class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, related_name='attributes', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100)