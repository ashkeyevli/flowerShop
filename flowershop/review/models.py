import datetime

from django.db import models

# Create your models here.
from _auth.models import Customer
from _auth.models import Manager


class Comment(models.Model):
    description = models.TextField(verbose_name='Описание', null=True)
    created_date = models.DateField(verbose_name='Дата создания', default= datetime.date.today)

    class Meta:
        abstract = True




class Review(Comment):
    customer = models.ForeignKey(Customer, verbose_name='Автор', on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=255, verbose_name='Наименование')
    rate = models.PositiveIntegerField('Качество обслуживание', default=0)
#
class Reply(Comment):
    review = models.ForeignKey(Review, verbose_name='Отзыв', on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, verbose_name='Автор', on_delete=models.CASCADE, related_name='replies')
#     created_date = models.DateField(verbose_name='Дата ответа', default= datetime.date.today)
#     description = models.TextField(verbose_name='Описание', null=True)