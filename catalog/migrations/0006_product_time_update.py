# Generated by Django 5.0.4 on 2024-04-29 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_time_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата последнего изменения'),
        ),
    ]