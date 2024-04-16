# views.py
from django.shortcuts import render, redirect
from .models import Object
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import date, timedelta
from .models import MyObject, MyCurrentObject
from .models import Product # модель прайса
from .models import Note  # модель записок
from django.views.generic import ListView, DetailView # подключаем модель для каталога

from .models import MyObject
from .forms import MyObjectForm
from .models import MyCurrentObject

def home(request):
    objects = Object.objects.all()
    return render(request, 'home.html', {'objects': objects})


def add_item(request):
    objects = Object.objects.all()
    return render(request, 'add_item.html', {'objects': objects})

def add_new(request):
    if request.method == 'POST':
        form = MyObjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_new')  # Перенаправление на эту же страницу после успешного сохранения объекта
    else:
        form = MyObjectForm()
    objects = Object.objects.all()
    return render(request, 'add_new.html', {'form': form, 'objects': objects})


def catalog(request):
    objects = Object.objects.all()
    return render(request, 'catalog.html', {'objects': objects})

def my_object(request):
    objects = Object.objects.all()
    return render(request, 'my_object.html', {'objects': objects})

def profile(request):
    objects = Object.objects.all()
    return render(request, 'profile.html', {'objects': objects})

def create_note(request):
    if request.method == 'POST':
        # Если форма отправлена методом POST
        title = request.POST['title']
        content = request.POST['content']
        
        # Создаем новую заметку и сохраняем в базу данных
        new_note = Note(title=title, content=content)
        new_note.save()
        
        # После сохранения перенаправляем пользователя, например, на главную страницу
        return redirect('home')  # 'home' - это имя URL-шаблона для главной страницы
    else:
        # Если запрос не методом POST, просто отображаем форму для создания заметки
        return render(request, 'create_note.html')  # 'create_note.html' - это шаблон для страницы создания заметки



        # добавляем новый элемент (услуга)
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


   
        # добавляем новый объект
def create_object(request):
    if request.method == 'POST':
        form = MyObjectForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('object_list')  # Перенаправление на страницу со списком объектов
    else:
        form = MyObjectForm()
        return render(request, 'add_new.html', {'form': form})
  


    # текущий объект
def mycurrentobject(request):
    objects = MyCurrentObject.get_objects()
    return render(request, 'mycurrentobject.html', {'objects': objects})






