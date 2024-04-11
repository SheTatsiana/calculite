# urls.py
from django.urls import path, re_path
from .views import home
from .views import add_item
from .views import add_new
from .views import create_note
from .views import catalog
from .views import my_object
from .views import profile
from .views import ProductListView, ProductDetailView
from . import views
from .views import create_object
from .views import MyCurrentObject

urlpatterns = [
  
    path('home', home, name='home'),
    path('add_item', add_item, name='add_item'),
    path('add_new', add_new, name='add_new'),
    path('catalog', catalog, name='catalog'),
    path('my_object', my_object, name='my_object'),
    path('profile', profile, name='profile'),
    
    # создания заметки
    path('note', create_note, name='create_note'),

    # создание прайса
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    
    path('create/', create_object, name='create_object'),
    path('MyCurrentObject', MyCurrentObject, name='MyCurrentObject'),

   ]

