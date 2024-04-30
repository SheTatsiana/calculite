# views.py

from django.shortcuts import render, redirect
from .models import Object
from django.utils import timezone
from datetime import date, timedelta
from django.views.generic import ListView, DetailView
from django.db import models
from django.shortcuts import get_object_or_404
from .forms import MyObjectForm
from .models import MyCurrentObject, MyObject, Note, Product, WorkDetail, Profile

def home(request):
    my_current_objects = MyCurrentObject.objects.all()
    return render(request, 'home.html', {'my_current_objects': my_current_objects})

def mycurrentobject(request):
    my_current_objects = MyCurrentObject.objects.all()
    return render(request, 'mycurrentobject.html', {'my_current_objects': my_current_objects})

def my_view(request):
    current_objects = MyCurrentObject.get_objects()
    return render(request, 'mycurrentobject.html', {'current_objects': current_objects})

def my_object(request):
    my_objects = MyObject.objects.all()
    return render(request, 'my_object.html', {'my_objects': my_objects})

def note(request):
    notes = Note.objects.all()
    return render(request, 'note.html', {'notes': notes})

def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def workdetail(request):
    work_details = WorkDetail.objects.all()
    return render(request, 'workdetail.html', {'work_details': work_details})

def profile(request):
    profiles = Profile.objects.all()
    return render(request, 'profile.html', {'profiles': profiles})

def add_mco(request):
    if request.method == 'POST':
        # Обработка отправленной формы и перенаправление на mycurrentobject
        return redirect('mycurrentobject', permanent=True)
    else:
        # Отображение формы для добавления MyCurrentObject
        return render(request, 'add_mco.html')

def add_mo(request):
    if request.method == 'POST':
        return redirect('my_object')
    else:
        return render(request, 'add_mo.html')

def add_note(request):
    if request.method == 'POST':
        return redirect('note')
    else:
        return render(request, 'add_note.html')

def add_product(request):
    if request.method == 'POST':
        return redirect('product')
    else:
        return render(request, 'add_product.html')

def add_wd(request):
    if request.method == 'POST':
        return redirect('workdetail')
    else:
        return render(request, 'add_wd.html')

def add_profile(request):
    if request.method == 'POST':
        return redirect('profile')
    else:
        return render(request, 'add_profile.html')

def edit_mco(request):
    if request.method == 'POST':
        return redirect('mycurrentobject', permanent=True)
    else:
        return render(request, 'edit_mco.html')

def edit_mo(request):
    if request.method == 'POST':
        return redirect('my_object')
    else:
        return render(request, 'edit_mo.html')

def edit_note(request):
    if request.method == 'POST':
        return redirect('note')
    else:
        return render(request, 'edit_note.html')

def edit_product(request):
    if request.method == 'POST':
        return redirect('product')
    else:
        return render(request, 'edit_product.html')

def edit_wd(request):
    if request.method == 'POST':
        return redirect('workdetail')
    else:
        return render(request, 'edit_wd.html')

def edit_profile(request):
    if request.method == 'POST':
        return redirect('profile')
    else:
        return render(request, 'edit_profile.html')
