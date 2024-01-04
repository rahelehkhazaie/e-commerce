from django.urls import path
from .import views


app_name = "account"
urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('otp', views.OtpView.as_view(), name='otp-check'),
    path('checkout', views.CheckoutView.as_view(), name='checkout'),
    path('contact', views.ContactView.as_view(), name='contact')
]
