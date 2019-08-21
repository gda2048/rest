from django.db import models
from django.contrib.auth.models import User
# from djoser.urls.base import User


class Room(models.Model):
    """Room chat model"""
    creator = models.ForeignKey(User, verbose_name='Создатель', on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name='Участник чата', related_name='invited_users')
    date = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = 'Комната чата'
        verbose_name_plural = 'Комнаты чата'


class Message(models.Model):
    """Chat model"""
    room = models.ForeignKey(Room, verbose_name='Комната чата', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Создатель', on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=5000)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение чата'
        verbose_name_plural = 'Сообщения чатов'
