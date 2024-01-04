from django.contrib import admin
from cart.models import Order, OrderItem, Coupon
from . import models


class OrderItemAdmin(admin.TabularInline):
    model = models.OrderItem

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_paid')
    inlines = (OrderItemAdmin,)
    filter = ('is_paid',)
    
admin.site.register(Coupon)
    