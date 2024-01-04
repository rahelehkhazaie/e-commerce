from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.contrib import messages
from cart.cart_session import Cart
from product.models import *
from cart.models import *


class CartDetail(View):
    def get(self, request):
        cart = Cart(request)
        if cart.total() == 0:
            messages.info(request, 'cart is empty')
        return render(request, 'cart/cart.html', {'cart' : cart})
    
    
class AddToCart(View):
    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        size, color, quantity = request.POST.get('size'), request.POST.get('color'), request.POST.get('quantity')
        cart = Cart(request)
        cart.add(product, quantity, color, size)
        return redirect('cart:cart-detail')
    
    
class OrderDetail(View):
    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        order_item = OrderItem.objects.filter(order=order)
        if order_item == None:
            return redirect('product:product-list')
        return render(request, 'cart/order.html', {'order' : order, 'messages' : messages})
    
    
class OrderCreation(View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total())
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], size=item['size'], color=item['color'], quantity=item['quantity'], price=int(float(item['price'])))
        cart.remove()
        return redirect('cart:order-detail', order.id)
 
    
class DeleteCart(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect('cart:cart-detail')   
    
    
class ApplyCoupon(View):
    def post(self, request, pk):
        order = Order.objects.get(id=pk)
        code = request.POST.get('code')
        coupon = Coupon.objects.get(name=code)
        if coupon and coupon.quantity !=0 :
            order.total_price -= order.total_price * coupon.amount/100
            order.save()
            coupon.quantity -= 1
            coupon.save()
        elif not coupon:
            pass
        elif coupon.quantity == 0:
            pass
        return redirect('cart:order-detail', order.id)