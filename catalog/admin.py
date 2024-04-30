from django.contrib import admin
from .models import Note, Product, MyObject, MyCurrentObject, WorkDetail, Profile
from django.utils.html import format_html


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
    list_display = ('name', 'price', 'description', 'display_image')  # добавьте 'display_image' в список отображаемых полей

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        else:
            return 'No Image'

    display_image.short_description = 'Image'  # задаем краткое описание для поля

    # добавьте это, чтобы миниатюра была кликабельной и открывала полное изображение
    def get_list_display(self, request):
        return ('name', 'price', 'description', 'display_image')

    def display_image(self, obj):
        if obj.image:
            return format_html('<a href="{}"><img src="{}" width="50" height="50" /></a>'.format(obj.image.url, obj.image.url))
        else:
            return 'No Image'

    display_image.short_description = 'Image'

@admin.register(MyObject)
class MyObjectAdmin(admin.ModelAdmin):
    pass

@admin.register(WorkDetail)
class WorkDetailAdmin(admin.ModelAdmin):
    list_display = ('my_current_object', 'product', 'quantity', 'unit_price', 'total_price')
    list_filter = ('my_current_object', 'product')
    search_fields = ('my_current_object__name', 'product__name')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('my_current_object', 'product')

@admin.register(MyCurrentObject)
class MyCurrentObjectAdmin(admin.ModelAdmin):
    inlines = [WorkDetailInline]
    list_display = ('my_object', 'start_date', 'end_date', 'total_amount')
    

    def start_date(self, obj):
        return obj.my_object.start_date
    
    def end_date(self, obj):
        return obj.my_object.end_date

    start_date.short_description = 'Дата начала'
    end_date.short_description = 'Дата окончания'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass