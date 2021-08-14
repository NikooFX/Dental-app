from django.db import models

# Create your models here.

class Slider(models.Model):
    blog = models.ForeignKey('blogs.Blogs', verbose_name='Bloq', on_delete=models.CASCADE)


    def __str__(self):
        return self.blog.headline
    class Meta:
        verbose_name = 'Bloq'
        verbose_name_plural = 'Bloq'
        ordering = ['-id']