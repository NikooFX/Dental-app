# Generated by Django 3.1.5 on 2021-02-27 21:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100, verbose_name='Bloq başlığı')),
                ('image', models.ImageField(blank=True, default=None, help_text='min. 1920*1080', upload_to='static/blog_images/', verbose_name='Şəkil (Ana səhifə)')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='static/blog_images/', verbose_name='Şəkil (Bloq)')),
                ('short_blog', models.CharField(help_text='İlk cümlə...', max_length=100, null=True, verbose_name='Qısa başlanğıc')),
                ('main_blog', ckeditor.fields.RichTextField(max_length=100000, verbose_name='Əsas bloq')),
                ('created_date', models.DateField(verbose_name='Tarix')),
            ],
            options={
                'verbose_name': 'Bloqlar',
                'verbose_name_plural': 'Bloqlar',
            },
        ),
    ]