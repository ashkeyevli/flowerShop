import os
import shutil


def category_image_directory_path(instance, filename):
    return f'category_photos/{instance.name}/{filename}'

def product_image_directory_path(instance, filename):
    return f'category_photos/{instance.title}/{filename}'


def manager_image_directory_path(instance, filename):
    return f'users/{instance.manager.role}/{instance.admin.username}/{filename}'

def admin_image_directory_path(instance, filename):
    return f'users/{instance.admin.role}/{instance.admin.username}/{filename}'

def admin_avatar_delete(filename):
    admin_avatar_path = os.path.abspath(os.path.join(filename.path, '../..'))
    shutil.rmtree(admin_avatar_path)

def manager_avatar_delete(filename):
    manager_avatar_path = os.path.abspath(os.path.join(filename.path, '../..'))
    shutil.rmtree(manager_avatar_path)

def category_photo_delete(filename):
    category_photo_path = os.path.abspath(os.path.join(filename.path, '../..'))
    shutil.rmtree(category_photo_path)

def flower_photo_delete(filename):
    # flower_photo_path = os.path.abspath(os.path.join(filename.path, '../..'))
    # print(flower_photo_path)
    shutil.rmtree(filename)