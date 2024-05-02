from django.db import models
from django.contrib.auth.models import User
import os
from datetime import datetime


def generate_filename(instance, filename):
    _, ext = os.path.splitext(filename)
    if instance.pk:
        filename = f"{instance.user.id}_{instance.user.username}{ext}"  # Используем ID пользователя в качестве части имени файла
    else:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}{ext}"
    return filename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=generate_filename, blank=True)  # Использую функцию generate_filename для генерации пути

    def __str__(self):
        return f'Profile for user {self.user.username}'


