# Generated by Django 3.1.6 on 2021-04-22 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210423_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default=None, upload_to='\\media', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='flower',
            name='image',
            field=models.ImageField(default=None, upload_to='\\media', verbose_name='Изображение'),
        ),
    ]
