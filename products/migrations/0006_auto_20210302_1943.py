# Generated by Django 3.1.5 on 2021-03-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_products_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='detail_main',
            field=models.TextField(max_length=800, verbose_name='Əsas məlumat'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Adı'),
        ),
    ]
