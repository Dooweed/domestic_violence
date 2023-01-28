from django.db import models


class UsernameId(models.Model):
    """ Mapping username -> id """
    username = models.CharField(max_length=128)
    telegram_id = models.BigIntegerField()
