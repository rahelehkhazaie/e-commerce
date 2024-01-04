from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from random import randint
from django.utils.crypto import get_random_string
from django.views.generic import View
from account.models import Otp, Address
from account.forms import LoginForm, CheckoutForm, RegisterForm, ContactForm, OtpForm, User
import ghasedakpack


sms = ghasedakpack.Ghasedak("b0b57dd4655e0fe43ab9670becd99d")


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form' : form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('account:checkout')
            else:
                form.add_error('phone', 'Invalid user data')
        else:
            form.add_error('phone', 'Invalid phone number')
            
        return render(request, 'account/login.html', {'form':form})
    
    
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form' : form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000, 9999)
            sms.verification({'receptor': cd['phone'],'type': '1','template': 'ellieshop','param1': randcode})
            token = get_random_string(length=50)
            Otp.objects.create(
                phone = cd['phone'],
                code = randcode,
                token = token 
            )
            print(randcode)
            return redirect(reverse('account:otp-check') + f"?token={token}" + f"username={cd['username']}")
        
        return render(request, 'account/register.html', {'form' : form})


class OtpView(View):
    def get(self, request):
        form = OtpForm()
        return render(request, 'account/otp.html', {'form' : form})
    
    def post(self, request):
        form = OtpForm(request.POST)
        token = request.GET.get('token')
        username = request.GET.get('username')
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['otp'], token=token.exists()):
                phone = Otp.objects.get(token=token)
                user = User.objects.create(phone=phone, username=username)
                login(request, user)
                return redirect('/')
        else:
            form.add_error('otp', 'Invalid data')
            
        return render(request, 'account/otp.html', {'form' : form})
   

class CheckoutView(View):
    def get(self, request):
        form = CheckoutForm()
        return render(request, 'account/checkout.html', {'form':form})
    
    def post(self, request):
        form = CheckoutForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            return redirect('/')
        return render(request, 'account/checkout.html', {'form':form})

    
class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'account/contact.html', {'form':form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('/')
        return render(request, 'account/contact.html', {'form':form})




    