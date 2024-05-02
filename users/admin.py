
from django.contrib import admin
from .models import Profile
from django.utils.html import format_html

#class ProfileAdmin(admin.ModelAdmin):
   # list_display = ['user', 'date_of_birth', 'photo']


#admin.site.register(Profile, ProfileAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'photo_thumbnail')  

    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />'.format(obj.photo.url))
        else:
            return 'No photo'

    photo_thumbnail.short_description = 'Photo'

admin.site.register(Profile, ProfileAdmin)
