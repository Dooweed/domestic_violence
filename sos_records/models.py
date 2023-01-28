from django.db import models


class SosRecord(models.Model):
    name = models.CharField('Имя', max_length=128)
    address = models.CharField('Адрес', max_length=300)
    phone = models.CharField('Тел. номер', max_length=20, null=True, blank=True)
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    shelter = models.ForeignKey(verbose_name='Шелтер', to='shelters.Shelter', on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка SOS'
        verbose_name_plural = 'Заявки SOS'
