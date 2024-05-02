from django import forms
from .models import MyObject, Note, Product, WorkDetail, MyCurrentObject



class MyCurrentObjectForm(forms.ModelForm):
    class Meta:
        model = MyCurrentObject
        fields = '__all__'

class MyObjectForm(forms.ModelForm):
    class Meta:
        model = MyObject
        fields = ['name']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']

class WorkDetailForm(forms.ModelForm):
    class Meta:
        model = WorkDetail
        fields = ['product', 'quantity']



