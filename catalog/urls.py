# urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('mycurrentobject/', views.mycurrentobject, name='mycurrentobject'),
    path('my_object', views.my_object, name='my_object'),
    path('note', views.note, name='note'),
    path('product', views.product, name='product'),
    path('workdetail', views.workdetail, name='workdetail'),
    
    path('add_mco', views.add_mco, name='add_mco'),
    path('add_mo', views.add_mo, name='add_mo'),
    path('add_note', views.add_note, name='add_note'),
    path('add_product', views.add_product, name='add_product'),
    path('add_wd', views.add_wd, name='add_wd'),
    
    path('edit_mco/<int:pk>/', views.edit_mco, name='edit_mco'),
    path('edit_mo/<int:pk>/', views.edit_mo, name='edit_mo'),
    path('edit_note/<int:pk>/', views.edit_note, name='edit_note'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('edit_wd/<int:pk>/', views.edit_wd, name='edit_wd'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
