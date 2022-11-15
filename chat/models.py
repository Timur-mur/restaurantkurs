from django.db import models

from django.contrib.auth.models import User


class Room(models.Model):
    admin = models.ForeignKey(User, verbose_name="Админ", on_delete=models.CASCADE)
    clients = models.OneToOneField(User, verbose_name="Клиент", related_name="client", on_delete=models.CASCADE)
    date = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = 'Комната поддержки'
        verbose_name_plural = 'Комнаты поддержки'


class Chat(models.Model):
    room = models.ForeignKey(Room, verbose_name="Комната поддержки", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=500)
    date = models.DateTimeField("Время отправки", auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение поддержки'
        verbose_name_plural = 'Сообщения поддержки'
