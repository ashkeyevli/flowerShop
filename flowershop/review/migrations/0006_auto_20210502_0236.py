# Generated by Django 3.1.6 on 2021-05-01 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_comment_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='comment_ptr',
        ),
        migrations.RemoveField(
            model_name='review',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]