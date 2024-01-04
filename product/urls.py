from django.urls import path
from product import views


app_name = 'product'
urlpatterns = [
    #path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('all/', views.ProductListView.as_view(), name='product-list'),
    path('navbar', views.NavbarPartialView.as_view(), name='navbar'),
    #path('topbar', views.TopbarPartialView.as_view(), name='topbar'),
    path('search', views.SearchResultView.as_view(), name='search-result'),
    path('<int:pk>/', views.productDetail, name='product-detail'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail')

    
    
]
