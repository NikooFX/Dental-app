# Generated by Django 3.1.5 on 2021-03-18 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210318_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='company',
            field=models.CharField(choices=[('all', 'Ümumi'), ('tepe', 'TePe'), ('bilimplant', 'Bilimplant'), ('miradent', 'Miradent')], default='all', help_text='Hansı saytda görünməsini istəyirsən?', max_length=15, null=True, verbose_name='Firma'),
        ),
    ]
