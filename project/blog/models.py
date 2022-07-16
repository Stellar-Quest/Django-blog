import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=150)
    text = models.TextField('Текст поста', max_length=10000)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    published = models.DateTimeField('Дата публикации', default=timezone.now)

    def __str__(self):
        return f'Пост: {self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_url(self):
        return reverse(
            'post',
            args=[self.id],
        )

    def was_published_recently(self):
        return self.published >= timezone.now() + datetime.timedelta(days=1)
