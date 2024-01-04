from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, DetailView, ListView
from product.models import *


class HomeView(ListView):
    model = Product
    template_name = "base/index.html"
    products = Product.objects.all()
    featured_products = products.filter(discount__gte=10)
    recent_products = products.all().order_by('created_at')
    categories = Category.objects.all()
    pros = Product.objects.exclude(is_special=False)
    
    extra_context= {
        'featured_products' : featured_products,
        'recent_products' : recent_products,
        'categories' : categories,
        'pros' : pros[0:2]
    }

    
