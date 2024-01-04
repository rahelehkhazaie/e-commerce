from django.db import models
from product.models import *
from account.models import User


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='orders')
    total_price = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)   
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders' )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    quantity = models.SmallIntegerField()
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.product
        
    
class Coupon(models.Model):
    amount = models.SmallIntegerField(default=0)
    name = models.CharField(max_length=50)
    quantity = models.SmallIntegerField()
    
    def __str__(self):
        return self.name

