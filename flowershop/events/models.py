from django.db import models

# Create your models here.
from _auth.models import Manager


class Event(models.Model):
    manager = models.ForeignKey(Manager, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    image = models.ImageField(upload_to='../flowershop/events/images/', default=None, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
    description = models.TextField(verbose_name='Описание', null=True)

    def __str__(self):
        return self.title