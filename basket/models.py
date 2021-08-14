from django.db import models
from products.models import Products
from django.contrib import admin
# Create your models here.

class Basket(models.Model):
    cookie_id = models.CharField(max_length=100)
    product_id = models.IntegerField()
    name = models.CharField('Adı', max_length=50)
    size = models.CharField('Ölçüsü', max_length=10)
    image = models.ImageField('Şəkil', upload_to='static/product_images/', default=None)
    price = models.DecimalField(verbose_name='Qiymət AZN', null=False, default=0.00, max_digits=6, decimal_places=2)
    count = models.IntegerField('Sayı', default=0,)

class Orders(models.Model):
    name = models.CharField('Sifarişçi', max_length=100)
    phone = models.CharField('Tel', max_length=50, null=True)
    address = models.CharField('Ünvan', max_length=50, null=True)
    product = models.TextField('Məhsullar', max_length=1000, null=True, blank=True)
    status = models.BooleanField('Yerinə yetirildi', default=False)
    created_date = models.DateField('Sifariş tarixi', auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sifarişlər'
        verbose_name_plural = 'Sifarişlər'
