from django.db import models

# Create your models here.
from _auth.models import Customer


class Review(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    rate = models.PositiveIntegerField('Качество обслуживание', default=0)
    description = models.TextField(verbose_name='Описание', null=True)

    def __str__(self):
        return self.title