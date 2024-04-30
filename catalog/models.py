# models.py
from django.db import models, transaction
from django.contrib import admin
from datetime import date
from django.utils import timezone
from decimal import Decimal
from django.contrib.auth.models import User


# модель Объект 
class Object(models.Model):
    name = models.CharField(max_length=200)
    dat_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

# модель Заметки
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=date.today)  # Поле даты с сегодняшней датой по умолчанию

    def __str__(self):
        return f"{self.title} ({self.date.strftime('%Y-%m-%d')})"


# модель Продукты
import os
from datetime import datetime

def generate_filename(instance, filename):
    _, ext = os.path.splitext(filename)
    if instance.pk:
        filename = f"{instance.pk}{ext}"  # Используем ID объекта в качестве имени файла
    else:
        # Если объект еще не сохранен в базе данных, используем текущую дату и время для генерации уникального имени файла
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}{ext}"
    return os.path.join("products", filename)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=generate_filename, blank=True, null=True)

    def __str__(self):
        return self.name


# модель для добавления объекта
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
    

# модель мой текущий объект
class MyCurrentObject(models.Model):
    my_object = models.ForeignKey(MyObject, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    
    @classmethod
    def get_objects(cls):
        return cls.objects.filter(my_object__end_date__gt=date.today())
   
    
    def update_total_price(self):
        # Вычисляем общую сумму по объекту
        total_price = WorkDetail.objects.filter(my_current_object=self).aggregate(models.Sum('total_price'))['total_price__sum'] or 0
        self.total_object_price = total_price
        self.save(update_fields=['total_object_price'])

    def __str__(self):
        return str(self.my_object)

    def calculate_total_amount(self):
        return sum(detail.total_price for detail in self.work_details.all())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.total_amount = self.calculate_total_amount()
        super().save(*args, **kwargs)


# модель рабочие детали (продукт + количество + цена + стоимость + фото)
class WorkDetail(models.Model):
    my_current_object = models.ForeignKey(MyCurrentObject, on_delete=models.CASCADE, related_name='work_details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.unit_price = self.product.price
        self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} - {self.total_price}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
  
    def __str__(self):
        return self.user.username