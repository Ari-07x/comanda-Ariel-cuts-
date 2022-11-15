# Generated by Django 4.1.3 on 2022-11-09 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('description', models.CharField(max_length=255)),
                ('sealing_price', models.FloatField()),
                ('status', models.BinaryField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(blank=True, max_length=80, null=True)),
                ('cuit', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=255)),
                ('sealing_price', models.FloatField()),
                ('cost_price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('status', models.BinaryField(max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('suppliers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyAPI.supplier')),
            ],
        ),
    ]