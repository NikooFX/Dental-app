from django.db import models
from ckeditor.fields import RichTextField
import random

# Create your models here.
class Products(models.Model):


    category_choices = [
        ('İnterdental fırçalar', (
            ('original', 'Orijinal'),
            ('extra_soft', 'Eksta yumşaq'),
            ('angle', 'Dönəcəkli'),
        )
         ),
        ('toothpicks', 'Kürdan'),
        ('dental_floss', 'Diş ipi'),
        ('brushers', (
            ('adult', 'Böyüklər üçün'),
            ('kids', 'Uşaqlar üçün')
        )),
        ('special_brushes', 'Xüsusi fırçalar'),
        ('accesories', 'Aksesuarlar')
    ]
    company_choices = [('all', 'Ümumi'), ('tepe', 'TePe'), ('bilimplant', 'Bilimplant'),  ('miradent', 'Miradent')]

    image1 = models.ImageField('Şəkil 1', upload_to='static/product_images/', default=None, help_text='425x425 ölçüsündə olmalıdır!')
    image2 = models.ImageField('Şəkil 2', upload_to='static/product_images/', default=None, help_text='425x425 ölçüsündə olmalıdır!')
    image3 = models.ImageField('Şəkil 3', upload_to='static/product_images/', default=None, help_text='425x425 ölçüsündə olmalıdır!')
    image4 = models.ImageField('Şəkil 4', upload_to='static/product_images/', default=None, help_text='425x425 ölçüsündə olmalıdır!')
    image5 = models.ImageField('Şəkil 5', upload_to='static/product_images/', default=None, help_text='425x425 ölçüsündə olmalıdır!')
    name = models.CharField('Adı', max_length=100)
    color = models.CharField('Rəngi', max_length=15)
    size = models.CharField('Ölçüsü', max_length=50)
    detail_mini = models.CharField('Qısa məlumat', max_length=180)
    detail_main = models.TextField('Əsas məlumat', max_length=800)
    #detail_main = RichTextField('Əsas məlumat', max_length=500)
    category = models.CharField(choices=category_choices, verbose_name='Kateqoriya', max_length=30)
    price = models.DecimalField(verbose_name='Qiymət AZN', null=False, default=0.00, max_digits=6, decimal_places=2)
    price_discount = models.DecimalField(verbose_name='Endirim', null=False, default=0.00, max_digits=6, decimal_places=2, help_text='Yoxdursa boş burax')
    discount = models.BooleanField(default=False, verbose_name='Endirimli')
    discount_precent = models.IntegerField('Faiz', null=True, default=0)
    status = models.BooleanField(default=True, verbose_name='Hər kəsə açıq')
    company = models.CharField(choices=company_choices, verbose_name='Firma', help_text='Hansı saytda görünməsini istəyirsən?', default='all', null=True, max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Məhsullar'
        verbose_name_plural = 'Məhsullar'

class Discounts(models.Model):
    name = models.CharField('Adı', max_length=20)
    precent = models.IntegerField('Endirim faizi %')
    end_date = models.DateField('Bitmə tarixi', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Endirimlər'
        verbose_name_plural = 'Endirimlər'
        ordering = ['id']

class Popular(models.Model):
    name = models.ForeignKey('products.Products', verbose_name='Ən çox satılan məhsullar', on_delete=models.PROTECT)

    def __str__(self):
        return self.name.name

    class Meta:
        verbose_name = 'Ən çox satılan məhsullar'
        verbose_name_plural = 'Ən çox satılan məhsullar'