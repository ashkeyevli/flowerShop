from django.db import models

# Create your models here.
from _auth.models import Manager


class Events(models.Model):
    manager = models.ForeignKey(Manager, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    image = models.ImageField(upload_to='../flowershop/events/images/', default=None, verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)

    def __str__(self):
        return self.title