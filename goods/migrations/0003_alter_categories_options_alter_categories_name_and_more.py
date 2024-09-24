# Generated by Django 5.0.1 on 2024-01-13 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_categories_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорію'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Назва')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Зображення')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Ціна')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Знижка %')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Кількість')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.categories', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукти',
                'db_table': 'product',
            },
        ),
    ]
