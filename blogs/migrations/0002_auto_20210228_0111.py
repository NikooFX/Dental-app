# Generated by Django 3.1.5 on 2021-02-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='img2',
        ),
        migrations.AddField(
            model_name='blogs',
            name='sekil2',
            field=models.ImageField(blank=True, default=None, upload_to='static/blog_images/', verbose_name='Şəkil (Blog)'),
        ),
    ]
