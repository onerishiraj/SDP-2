# Generated by Django 3.2.2 on 2021-05-14 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0012_alter_orders_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.date(2021, 5, 15)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='time',
            field=models.TimeField(default=datetime.time(0, 28, 24, 499417)),
        ),
    ]
