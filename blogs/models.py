from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blogs(models.Model):

    company_choices = [('all', 'Ümumi'), ('tepe', 'TePe'), ('bilimplant', 'Bilimplant'), ('miradent', 'Miradent')]

    headline = models.CharField('Bloq başlığı', max_length=100)
    image = models.ImageField('Şəkil (Ana səhifə)', upload_to='static/blog_images/', help_text='min. 1920*1080', default=None, blank=True)
    sekil2 = models.ImageField('Şəkil (Blog)', upload_to='static/blog_images/', default=None, blank=True)
    short_blog = models.CharField('Qısa başlanğıc', max_length=100, help_text='İlk cümlə...', null=True)
    main_blog = RichTextField('Əsas bloq', max_length=100000)
    created_date = models.DateField('Tarix')
    company = models.CharField(choices=company_choices, verbose_name='Firma', help_text='Hansı saytda görünməsini istəyirsən?', default='all', null=True, max_length=15)


    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = 'Bloqlar'
        verbose_name_plural = 'Bloqlar'