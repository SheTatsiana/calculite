from django.shortcuts import render, redirect, get_object_or_404
from .models import MyCurrentObject, MyObject, Note, Product, WorkDetail
from .forms import MyCurrentObjectForm
from django.urls import reverse
from .forms import ProductForm
from .forms import MyObjectForm

#url = reverse('users:profile_edit')

def home(request):
    my_current_objects = MyCurrentObject.objects.all()
    return render(request, 'home.html', {'my_current_objects': my_current_objects})

def mycurrentobject(request):
    my_current_objects = MyCurrentObject.objects.all()
    return render(request, 'mycurrentobject.html', {'my_current_objects': my_current_objects})

def my_view(request):
    current_objects = MyCurrentObject.get_objects()
    return render(request, 'mycurrentobject.html', {'current_objects': current_objects})

def my_object_view(request):
    objects = MyObject.objects.all()  # Получаем все объекты
    return render(request, 'my_object.html', {'objects': objects})

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


def add_mco(request):
    if request.method == 'POST':
        form = MyCurrentObjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mycurrentobject')
    else:
        form = MyCurrentObjectForm()
    return render(request, 'add_mco.html', {'form': form})

def add_mo(request):
    if request.method == 'POST':
        form = MyObjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_object')
    else:
        form = MyObjectForm()
    return render(request, 'add_mo.html', {'form': form})

def add_note(request):
    if request.method == 'POST':
        return redirect('note')
    else:
        return render(request, 'add_note.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')  # Перенаправляем на страницу со списком продуктов
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def add_wd(request):
    if request.method == 'POST':
        return redirect('workdetail')
    else:
        return render(request, 'add_wd.html')

def edit_mco(request, pk):
    my_current_object = get_object_or_404(MyCurrentObject, pk=pk)
    if request.method == 'POST':
        form = MyCurrentObjectForm(request.POST, instance=my_current_object)
        if form.is_valid():
            form.save()
            return redirect('mycurrentobject')
    else:
        form = MyCurrentObjectForm(instance=my_current_object)
    return render(request, 'edit_mco.html', {'form': form})

def edit_mo(request, pk):
    my_object = get_object_or_404(MyObject, pk=pk)
    if request.method == 'POST':
        form = MyObjectForm(request.POST, instance=my_object)
        if form.is_valid():
            form.save()
            return redirect('my_object')
    else:
        form = MyObjectForm(instance=my_object)
    return render(request, 'edit_mo.html', {'form': form})

def edit_note(request, pk):  
    if request.method == 'POST':
        return redirect('note')
    else:
        return render(request, 'edit_note.html')

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')  # Перенаправляем на страницу со списком продуктов
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

def edit_wd(request, pk):  
    if request.method == 'POST':
        return redirect('workdetail')
    else:
        return render(request, 'edit_wd.html')


def delete_product(request, pk):
    # Получаем объект продукта или возвращаем ошибку 404, если продукт не найден
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        # При получении POST-запроса удаляем продукт
        product.delete()
        # Перенаправляем пользователя на страницу со списком продуктов
        return redirect('product')
    # Возвращаем шаблон для подтверждения удаления продукта
    return render(request, 'delete_product.html', {'product': product})

def delete_mo(request, pk):
    my_object = get_object_or_404(MyObject, pk=pk)
    if request.method == 'POST':
        my_object.delete()
        return redirect('my_object')
    return render(request, 'delete_mo.html', {'my_object': my_object})
