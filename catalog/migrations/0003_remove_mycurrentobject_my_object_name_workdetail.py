# Generated by Django 5.0 on 2024-04-17 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_myobject_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycurrentobject',
            name='my_object_name',
        ),
        migrations.CreateModel(
            name='WorkDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('my_current_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.mycurrentobject')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
        ),
    ]