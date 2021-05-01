import datetime

from django.db import models

# Create your models here.
from _auth.models import Customer
from ordering.constants import DELIVERY_TYPE_CHOICE, STATUS_CHOICE, STATUS_NEW, DELIVERY_TYPE_PICKUP
from product.models import Flower





class Order(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='Покупатель', related_name='related_orders',
                                 on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=255, verbose_name='Имя')
    # last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    # phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    # address = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Счет к заказу')
    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    order_date = models.DateField(verbose_name='Дата получения заказа', default=datetime.date.today)
    status = models.CharField(
        max_length=100,
        verbose_name='Статус заказа',
        choices=STATUS_CHOICE,
        default=STATUS_NEW
    )
    delivery_type = models.CharField(
        max_length=100,
        verbose_name='Тип доставки',
        choices=DELIVERY_TYPE_CHOICE,
        default=DELIVERY_TYPE_PICKUP
    )

    def __str__(self):
        return self.items

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
