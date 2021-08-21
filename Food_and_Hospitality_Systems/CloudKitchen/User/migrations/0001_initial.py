# Generated by Django 3.2.2 on 2021-05-15 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0015_delivery_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('line1', models.CharField(max_length=100)),
                ('line2', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('zip', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.user')),
            ],
        ),
    ]