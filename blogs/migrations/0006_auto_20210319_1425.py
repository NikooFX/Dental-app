# Generated by Django 3.1.5 on 2021-03-19 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20210318_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogs',
            options={'ordering': ['-id'], 'verbose_name': 'Bloqlar', 'verbose_name_plural': 'Bloqlar'},
        ),
    ]