# Generated by Django 3.2.2 on 2021-05-15 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0015_orders_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]