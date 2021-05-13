from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from _auth.models import Customer, Manager, Admin, CustomerProfile, AdminProfile, ManagerProfile
from product.models import Category, Flower
from utils.upload import admin_avatar_delete, category_photo_delete, flower_photo_delete


@receiver(post_delete, sender = Category )
def delete_photo_on_category_delete(sender, instance, **kwargs):
    photo = instance.image
    if photo:
        category_photo_delete(photo)

@receiver(post_delete, sender = Flower )
def delete_photo_on_flower_delete(sender, instance, **kwargs):
    photo = instance.image
    if photo:
        flower_photo_delete(photo)