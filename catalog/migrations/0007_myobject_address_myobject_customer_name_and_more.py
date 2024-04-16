# Generated by Django 5.0 on 2024-04-16 09:34

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_rename_myobject_mycurrentobject_my_object_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myobject',
            name='address',
            field=models.CharField(default='Vilnius', max_length=255),
        ),
        migrations.AddField(
            model_name='myobject',
            name='customer_name',
            field=models.CharField(default='Name', max_length=255),
        ),
        migrations.AddField(
            model_name='myobject',
            name='documents',
            field=models.FileField(default='documents/default.jpg', upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='myobject',
            name='executor_name',
            field=models.CharField(default='Valery', max_length=255),
        ),
        migrations.AddField(
            model_name='myobject',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mycurrentobject',
            name='my_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.myobject'),
        ),
    ]
