# models.py
from django.db import models
from django.contrib import admin
from datetime import date
from django.utils import timezone


# модель для добавления 
class Object(models.Model):
    name = models.CharField(max_length=200)
    dat_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    


# модель "Note"
class Note(models.Model):
    # Поле для заголовка текста и даты заметки
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# модель Product с двумя полями: name (наименование) и price (цена).
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# добавляем модель для добавления объекта
class MyObject(models.Model):
    address = models.CharField(max_length=255, default='Vilnius')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    customer_name = models.CharField(max_length=255, default='Name')
    executor_name = models.CharField(max_length=255, default='Valery')
    documents = models.FileField(upload_to='documents/', default='documents/Договор_Visatos_Platuma_Valery.pdf')

 
    @classmethod
    def get_objects(cls):
        return cls.objects.filter(end_date__gt=date.today())


# модель для списка текущих объектов
class MyCurrentObject(models.Model):
    my_object = models.ForeignKey(MyObject, on_delete=models.CASCADE)
    my_object_name = models.CharField(max_length=100, default='none')

    @classmethod
    def get_objects(cls):
        return cls.objects.filter(my_object__end_date__gt=date.today())


