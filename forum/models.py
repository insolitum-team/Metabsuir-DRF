from django.contrib.auth.models import User
from django.db import models


class Section(models.Model):
    name = models.CharField('Название секции', max_length=255)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField('Название темы', max_length=255)
    date = models.DateTimeField('Дата создания', auto_now_add=True)
    main_post = models.TextField('Основная информация')
    author = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField('Содержание')
    theme = models.ForeignKey(Theme, blank=False, null=False, on_delete=models.CASCADE)
    reply_to = models.IntegerField('Ответ на', blank=True, null=True)
    sender = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField('Дата отправки', auto_now_add=True)


class SideMenuItem(models.Model):
    theme = models.ForeignKey(Theme, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.theme.name
