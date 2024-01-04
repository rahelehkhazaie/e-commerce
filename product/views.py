from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DetailView, ListView, TemplateView, CreateView
from django.urls import reverse, reverse_lazy
from itertools import chain
from django.core.paginator import Paginator
from django.db.models import Q
from product.models import *


"""class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'"""

    
class NavbarPartialView(TemplateView):
    template_name = 'includes/navbar.html'
    
    def get_context_data(self, **kwargs):
        context = super(NavbarPartialView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
    
    
class SearchResultView(View):
    def get(self, request):
        q = request.GET.get('q') if request.GET.get('q') != None else ''
        products = Product.objects.filter(
        Q(name__icontains=q) |
        Q(description__icontains=q))
        return render(request, 'product/search_result.html', {'products':products})
      
    
class ProductListView(ListView):
    model = Product
    template_name = 'product/shop.html'
    extra_context={'colors': Color.objects.all(),
                   'sizes': Size.objects.all()}
    
    def get_context_data(self, **kwargs):
        request = self.request
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')
        min_price = request.GET.get('min')
        max_price = request.GET.get('max')
        queryset = Product.objects.all()
        if colors:
            queryset = queryset.filter(color__title__in='colors').distinct()
        if sizes:
            queryset = queryset.filter(size__title__in='sizes').distinct()
        if min_price and max_price:
            queryset = queryset.filter(og_price__lte=max_price, og_price__gte=min_price)
        page_num = request.GET.get('page')
        paginator = Paginator(queryset, 1)
        page = paginator.get_page(page_num)
        context = super().get_context_data(**kwargs)
        context['object_list'] = page
        return context
    
    
def productDetail(request, pk):
    product = Product.objects.get(id=pk)
    cat_list = product.category.values_list()
    pros = Product.objects.all()
    for cat in cat_list:
        pros= pros.filter(category=cat).distinct()
        related_category= pros.exclude(id=product.id)
        
    if request.method == 'POST':
        message = Review.objects.create(
            user=request.user,
            product=product,
            body=request.POST.get('body')
        )
        return redirect(request.path)
    
    context = {
        'product' : product,
        'related_categories' : related_category
    }
    print(related_category)
    return render(request, 'product/detail.html', context)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'product/category_detail.html'
    



