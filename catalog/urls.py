from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

# Импортируем все необходимые представления 

from .views import (
    home_view,
    mycurrentobject,
    my_object,
    note,
    product,
    workdetail,
    create_work_detail,
    add_mco,
    edit_mco,
    add_mo,
    add_note,
    add_product,
    add_wd,
    edit_mo,
    edit_note,
    edit_product,
    edit_wd,
    delete_product,
    delete_mo,
    delete_note,
    delete_wd,
    delete_mco,
    export_to_excel,
    export_current_objects_to_excel,
    export_all_objects_to_excel,
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # главная с галереей и формой
    path('home/', views.home_view),          # дополнительный путь (необязательно)
    path('mycurrentobject/', views.mycurrentobject, name='mycurrentobject'),
    path('my_object/', views.my_object, name='my_object'),
    path('note/', views.note, name='note'),
    path('product/', views.product, name='product'),
    
    # Маршруты для работы с рабочими деталями
    path('workdetail', workdetail, name='workdetail'),
    path('workdetails/', workdetail, name='workdetail'),
    path('workdetails/add/', create_work_detail, name='create_work_detail'),
    path('add_wd', add_wd, name='add_wd'),
    path('edit_wd/<int:pk>/', edit_wd, name='edit_wd'),
    path('delete_wd/<int:pk>/', delete_wd, name='delete_wd'),
    
    # Маршруты для mycurrentobject
    path('add-mco', add_mco, name='add_mco'),
    path('edit_mco/<int:pk>/', edit_mco, name='edit_mco'),
    path('delete_mco/<int:pk>/', delete_mco, name='delete_mco'),
    
    # Маршруты для my_object
    path('add_mo', add_mo, name='add_mo'),
    path('edit_mo/<int:pk>/', edit_mo, name='edit_mo'),
    path('my_object/<int:pk>/delete/', delete_mo, name='delete_mo'),
    
    # Маршруты для note
    path('add_note', add_note, name='add_note'),
    path('edit_note/<int:pk>/', edit_note, name='edit_note'),
    path('delete_note/<int:pk>/', delete_note, name='delete_note'),
    
    # Маршруты для product
    path('add_product', add_product, name='add_product'),
    path('edit_product/<int:pk>/', edit_product, name='edit_product'),
    path('product/<int:pk>/delete/', delete_product, name='delete_product'),
    path('products/', product, name='products'),
    
    # Маршруты для экспорта данных
    path('export-to-excel/', export_to_excel, name='export_to_excel'),
    path('export_current_objects_to_excel/', export_current_objects_to_excel, name='export_current_objects_to_excel'),
    path('export_all_objects_to_excel/', export_all_objects_to_excel, name='export_all_objects_to_excel'),
    
] + static(settings.DOCUMENTS_URL, document_root=settings.DOCUMENTS_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
