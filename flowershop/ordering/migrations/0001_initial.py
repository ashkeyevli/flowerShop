# Generated by Django 3.1.6 on 2021-04-30 15:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0012_auto_20210427_0118'),
        ('_auth', '0002_auto_20210423_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Счет к заказу')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')),
                ('order_date', models.DateField(default=datetime.date.today, verbose_name='Дата получения заказа')),
                ('status', models.CharField(choices=[('new', 'Новый заказ'), ('in_progress', 'Заказ в обработке'), ('ready', 'Заказ готов к доставке'), ('completed', 'Заказ выполнен')], default='new', max_length=100, verbose_name='Статус заказа')),
                ('delivery_type', models.CharField(choices=[('pickup', 'Самовывоз'), ('delivery', 'Доставка курьером')], default='pickup', max_length=100, verbose_name='Тип доставки')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='_auth.customer', verbose_name='Покупатель')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ordering.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='product.flower')),
            ],
        ),
    ]
