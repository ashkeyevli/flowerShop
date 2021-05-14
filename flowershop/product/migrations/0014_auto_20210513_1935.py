# Generated by Django 3.1.6 on 2021-05-13 13:35

from django.db import migrations, models
import utils.upload
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20210512_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=utils.upload.category_image_directory_path, validators=[utils.validators.validate_size, utils.validators.validate_extension], verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='flower',
            name='image',
            field=models.ImageField(default=None, upload_to='flowers', verbose_name='Изображение'),
        ),
    ]
