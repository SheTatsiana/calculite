# models.py
from django.db import models
from django.contrib import admin
from datetime import date
from django.utils import timezone
from decimal import Decimal



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
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        if self.name:
            return f"{self.name} ({self.address})"
        return self.address

    @classmethod
    def get_objects(cls):
        return cls.objects.filter(end_date__gt=date.today())

class MyCurrentObject(models.Model):
    my_object = models.ForeignKey(MyObject, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    @classmethod
    def get_objects(cls):
        return cls.objects.filter(my_object__end_date__gt=date.today())
    
    def __str__(self):
        return str(self.my_object)

    def calculate_total_amount(self):
        return sum(detail.total_price for detail in self.work_details.all())

    def save(self, *args, **kwargs):
        self.total_amount = self.calculate_total_amount()
        super().save(*args, **kwargs)

class WorkDetail(models.Model):
    my_current_object = models.ForeignKey('MyCurrentObject', on_delete=models.CASCADE, related_name='work_details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} - {self.total_price}"

