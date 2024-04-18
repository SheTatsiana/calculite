from django.contrib import admin
from .models import Note, Product, MyObject, MyCurrentObject, WorkDetail

# Определение инлайн-классов

class WorkDetailInline(admin.TabularInline):
    model = WorkDetail
    extra = 1  # количество дополнительных форм для добавления

# Регистрируем модели

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(MyObject)
class MyObjectAdmin(admin.ModelAdmin):
    pass

@admin.register(WorkDetail)
class WorkDetailAdmin(admin.ModelAdmin):
    pass

@admin.register(MyCurrentObject)
class MyCurrentObjectAdmin(admin.ModelAdmin):
    inlines = [WorkDetailInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.save()
