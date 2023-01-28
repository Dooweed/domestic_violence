from django.db import models


class UsernameId(models.Model):
    """ Mapping username -> id """
    username = models.CharField('Юзернейм', max_length=128)
    telegram_id = models.BigIntegerField('Телеграм ID')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Привязка юзернейма и ID'
        verbose_name_plural = 'Привязки юзернейма и ID'
