# Generated by Django 3.1.5 on 2021-03-19 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0002_auto_20210302_1932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['-id'], 'verbose_name': 'Bloq', 'verbose_name_plural': 'Bloq'},
        ),
    ]
