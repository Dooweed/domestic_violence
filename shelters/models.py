from django.db import models


class Shelter(models.Model):
    name = models.CharField('Название', max_length=120)
    address = models.CharField('Адрес', max_length=300)
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return self.name

    @property
    def location(self):
        return self.latitude, self.longitude

    class Meta:
        verbose_name = 'Шелтер'
        verbose_name_plural = 'Шелтеры'


class ShelterContactInfo(models.Model):
    shelter = models.ForeignKey(verbose_name='Шелтер', to='shelters.Shelter', on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=120)
    email = models.EmailField('Эл. почта', null=True, blank=True)
    phone = models.CharField('Тел. номер', max_length=20, null=True, blank=True)
    telegram = models.CharField('Телеграм юзернейм', max_length=120, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'
