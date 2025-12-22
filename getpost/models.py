from django.utils import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст Новости')
    slug = models.SlugField('Ссылка', unique=True)
    created_ta = models.DateTimeField('Дата создания поста', default=timezone.now)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def __str__(self):
        return self.title