﻿from django import forms
from .models import MyObject



class MyObjectForm(forms.ModelForm):
       class Meta:
           model = MyObject
           fields = '__all__'

class MyCurrentObjectForm(forms.ModelForm):
       class Meta:
           model = MyObject
           fields = '__all__'        