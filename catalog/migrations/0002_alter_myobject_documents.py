# Generated by Django 5.0 on 2024-05-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myobject',
            name='documents',
            field=models.FileField(default='Договор_Visatos_Platuma_Valery.pdf', upload_to='documents/'),
        ),
    ]