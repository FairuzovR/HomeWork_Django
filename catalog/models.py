from django.db import models

NULLABLE = {'blank' : True, 'null' : True}

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    description = models.TextField(max_length=10000, verbose_name='Описание')
    images = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category =  models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='products',
                                  verbose_name='Категория')
    price = models.IntegerField (verbose_name='Цена за покупку', null=True)
    time_create = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания', null=True)
    time_update = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата последнего изменения', null=True)

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category', 'price']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование категории')
    description = models.TextField(max_length=10000, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
