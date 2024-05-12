from django.db import models

NULLABLE = {'blank' : True, 'null' : True}

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    description = models.TextField(max_length=10000, verbose_name='содержимое')
    slug = models.CharField(max_length=150, verbose_name='ссылка')
    images = models.ImageField(upload_to='blog/photo', verbose_name='изображение', **NULLABLE)
    time_create = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='дата создания', null=True)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'заголовок'
        verbose_name_plural = 'заголовоки'


