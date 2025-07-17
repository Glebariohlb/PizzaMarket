from django.db import models
from django.urls import reverse


# Create your models here.
class Pizzashop(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    is_published = models.BooleanField(default=True, verbose_name="Статус")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name = 'posts', verbose_name="Категории")
    ostrota = models.OneToOneField('Ostrota', on_delete=models.SET_NULL, null=True, blank=True, related_name='ostriy', verbose_name='ostrota')

    class Meta:
        verbose_name = 'Очень вкусные пиццы'
        verbose_name_plural = 'Очень вкусные пиццы'


    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create']),
        ]


    def __str__(self):
        return self.title


class Ostrota(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Уровень остроты")
    lvl = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PublishedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


    def __str__(self):
        return self.name