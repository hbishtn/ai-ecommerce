from django.urls import path
from .import views
from .api_views import product_list
urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    
    #api
    path('api/products/', product_list, name='api_products'),
]
