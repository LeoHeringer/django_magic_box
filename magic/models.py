# Arquivo: magic/models.py

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image_url = models.URLField(max_length=200, blank=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Box(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    products = models.ManyToManyField(Product, related_name='boxes')
    
    subscription_type = models.CharField(max_length=50, choices=[
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('activate', 'Active'),
        ('canceled', 'Canceled'),
        ('expired', 'Expired'),
    ])
    shipping_address = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.box.title}'

class Shipment(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    shipment_date = models.DateTimeField()
    tracking_number = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[
        ('shipped', 'Shipped'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('returned', 'Returned'),
    ])

    def __str__(self):
        return f'Shipment {self.tracking_number} for {self.subscription}'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'Review {self.user.username} for {self.box.title}'

class Promotion(models.Model):
    code = models.CharField(max_length=50)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.code
