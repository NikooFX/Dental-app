# Generated by Django 3.1.5 on 2021-01-26 19:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(default=None, upload_to='static/product_images/', verbose_name='Şəkil 1')),
                ('image2', models.ImageField(default=None, upload_to='static/product_images/', verbose_name='Şəkil 2')),
                ('image3', models.ImageField(default=None, upload_to='static/product_images/', verbose_name='Şəkil 3')),
                ('image4', models.ImageField(default=None, upload_to='static/product_images/', verbose_name='Şəkil 4')),
                ('image5', models.ImageField(default=None, upload_to='static/product_images/', verbose_name='Şəkil 5')),
                ('name', models.CharField(max_length=50, verbose_name='Adı')),
                ('color', models.CharField(max_length=15, verbose_name='Rəngi')),
                ('size', models.CharField(max_length=10, verbose_name='Ölçüsü')),
                ('detail_mini', models.CharField(max_length=180, verbose_name='Qısa məlumat')),
                ('detail_main', ckeditor.fields.RichTextField(max_length=500, verbose_name='Əsas məlumat')),
                ('category', models.CharField(choices=[('İnterdental fırçalar', (('original', 'Orijinal'), ('extra_soft', 'Eksta yumşaq'), ('angle', 'Dönəcəkli'))), ('toothpicks', 'Kürdan'), ('dental_floss', 'Diş ipi'), ('brushers', (('adult', 'Böyüklər üçün'), ('kids', 'Uşaqlar üçün'))), ('special_brushes', 'Xüsusi fırçalar'), ('accesories', 'Aksesuarlar')], max_length=30, verbose_name='Kateqoriya')),
                ('price', models.FloatField(default=0.0, verbose_name='Qiymət AZN')),
                ('stock', models.BooleanField(default=True, verbose_name='Stokda mövcudluğu')),
                ('status', models.BooleanField(default=True, verbose_name='Məhsulu aktiv et')),
            ],
            options={
                'verbose_name': 'Məhsullar',
                'verbose_name_plural': 'Məhsullar',
            },
        ),
    ]
