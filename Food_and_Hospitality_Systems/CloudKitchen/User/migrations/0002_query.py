# Generated by Django 3.2.2 on 2021-05-16 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_delivery_password'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=1000)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.user')),
            ],
        ),
    ]