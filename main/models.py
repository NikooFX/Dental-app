from django.db import models

# Create your models here.

class Calls(models.Model):
    name = models.CharField('Müştəri', max_length=50)
    phone = models.CharField('Tel', max_length=20)
    message = models.CharField('İstək mətni', max_length=200)
    created_date = models.DateTimeField('Tarix', auto_now_add=True)
    status = models.BooleanField('Zəng olundu', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Zəng gözləyən müştərilər'
        verbose_name_plural = 'Zəng gözləyən müştərilər'