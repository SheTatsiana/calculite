﻿from django import forms
from .models import MyObject, Note, Product, WorkDetail, MyCurrentObject



class MyCurrentObjectForm(forms.ModelForm):
    class Meta:
        model = MyCurrentObject
        fields = '__all__'

class MyObjectForm(forms.ModelForm):
    class Meta:
        model = MyObject
        fields = ['name', 'address', 'start_date', 'end_date', 'customer_name', 'executor_name', 'documents']
        labels = {
            'name': 'Название',
            'address': 'Адрес',
            'start_date': 'Начало проекта',
            'end_date': 'Окончание проекта',
            'customer_name': 'Заказчик',
            'executor_name': 'Исполнитель',
            'documents': 'Документы',
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']
        labels = {
            'name': 'Название',
            'price': 'Цена',
            'description': 'Описание',
            'image': 'Изображение',
        }

class WorkDetailForm(forms.ModelForm):
    class Meta:
        model = WorkDetail
        fields = ['product', 'quantity']



