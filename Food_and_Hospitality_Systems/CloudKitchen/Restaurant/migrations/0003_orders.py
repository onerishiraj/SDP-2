# Generated by Django 3.2.2 on 2021-05-14 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_delivery'),
        ('Restaurant', '0002_category_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_number', models.IntegerField(primary_key=True, serialize=False)),
                ('items', models.CharField(max_length=500)),
                ('quantity', models.CharField(max_length=50)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('accepted', models.BooleanField(default=False)),
                ('food_is_being_prepared', models.BooleanField(default=False)),
                ('ready_for_delivery', models.BooleanField(default=False)),
                ('picked_up', models.BooleanField(default=False)),
                ('out_for_delivery', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.user')),
            ],
        ),
    ]
