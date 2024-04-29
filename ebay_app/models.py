from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=False)
    description = models.TextField()
    category = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    waiting = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    remaining_time = models.IntegerField()
    last_bid = models.CharField(max_length=100, null=True, blank=True)
    highest_bid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    forPeople = models.BooleanField(default=False)
    forBot = models.BooleanField(default=False)
    bids_count = models.IntegerField(default=0)

    
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product.name + ' Image'
