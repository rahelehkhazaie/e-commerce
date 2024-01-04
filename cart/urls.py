from django.urls import path
from cart import views


app_name = 'cart'
urlpatterns = [
    path('detail', views.CartDetail.as_view(), name='cart-detail'),
    path('add/<int:pk>/', views.AddToCart.as_view(), name='add'),
    path('delete/<str:id>/', views.DeleteCart.as_view(), name='delete'),
    path('order/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),  
    path('order/add', views.OrderCreation.as_view(), name='order-creation'),    
    path('coupon/<int:pk>/', views.ApplyCoupon.as_view(), name='coupon'), 
]
