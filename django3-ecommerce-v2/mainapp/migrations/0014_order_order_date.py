# Generated by Django 3.0.8 on 2021-01-20 21:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_remove_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата получения заказа'),
        ),
    ]