# urls.py

from django.urls import path
from . import views
from .views import (
    home, add_item, add_new, create_note, catalog, my_object, profile,
    ProductListView, ProductDetailView, create_object, my_current_object_detail
)

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
    
    path('mycurrentobject/', views.mycurrentobject, name='mycurrentobject'),

    # Детали текущего объекта
    path('mycurrentobject/<int:object_id>/', views.my_current_object_detail, name='my_current_object_detail'),

]
