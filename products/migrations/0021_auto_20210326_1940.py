# Generated by Django 3.1.5 on 2021-03-26 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_discounts_end_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discounts',
            options={'ordering': ['-id'], 'verbose_name': 'Endirimlər', 'verbose_name_plural': 'Endirimlər'},
        ),
    ]
