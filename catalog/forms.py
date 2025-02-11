from django import forms
from .models import MyObject, Note, Product, WorkDetail, MyCurrentObject
from django.forms import modelformset_factory





class MyCurrentObjectForm(forms.ModelForm):
    class Meta:
        model = MyCurrentObject
        fields = ['my_object']

class MyObjectForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = MyObject
        fields = ['name', 'address', 'start_date', 'end_date', 'customer_name', 'executor_name', 'documents', 'products']
        labels = {
            'name': 'Название',
            'address': 'Адрес',
            'start_date': 'Начало проекта',
            'end_date': 'Окончание проекта',
            'customer_name': 'Заказчик',
            'executor_name': 'Исполнитель',
            'documents': 'Документы',
            'products': 'Продукты',
            'Currently': 'Редактировать'
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()  # сохраняем связанные продукты
        return instance

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}) 
        }
        labels = {
            'title': 'Название',
            'content': 'Описание',
            'date': 'Дата',
        }

  


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
        fields = ['my_current_object', 'product', 'quantity']

WorkDetailFormSet = modelformset_factory(WorkDetail, form=WorkDetailForm, extra=5)

class SelectCurrentObjectForm(forms.Form):
    my_current_object = forms.ModelChoiceField(queryset=MyCurrentObject.objects.all(), label='Выберите текущий объект')

WorkDetailFormSet = modelformset_factory(WorkDetail, form=WorkDetailForm, extra=3)


from .models import Gallery

class GalleryForm(forms.ModelForm):
    class Meta:
           model = Gallery
           fields = ['title', 'description', 'image']