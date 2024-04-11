from django.contrib import admin

# Ваш приложение/admin.py

from .models import Note

# Регистрируем модель Note 
admin.site.register(Note)


# Регистрируем модель Product 

from .models import Product

admin.site.register(Product)


# Регистрируем модель Мои объекты
from .models import MyObject

admin.site.register(MyObject)

# модель текущие объекты
from .models import MyCurrentObject

admin.site.register(MyCurrentObject)

