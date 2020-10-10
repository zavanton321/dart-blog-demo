from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Опублиновано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, width_field=300, height_field=200)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
