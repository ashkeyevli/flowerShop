from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from .constants import CUSTOMER_ROLE_ORDINARY, USER_ROLE_CUSTOMER, CUSTOMER_ROLES, USER_ROLES, USER_ROLE_ADMIN, USER_ROLE_MANAGER

class MainUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fiels):
        if not username:
            raise ValueError('set username')
        user = self.model(username= username, **extra_fiels)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password = None, **extra_fiels):
        extra_fiels.setdefault('is_superuser', True)
        return self._create_user(username, password, **extra_fiels)

    def create_superuser(self, username, password=None, **extra_fiels):
        extra_fiels.setdefault('is_superuser', True)
        if extra_fiels.get('is_superuser') is not True:
            raise ValueError('it is not superuser')
        return self._create_user(username, password, **extra_fiels)

class CustomerManager(MainUserManager):
    def create_customer(self, username, password=None, **extra_fiels):
        extra_fiels.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fiels)

# class StaffManager(MainUserManager):
#     def create_stuff(self, username, password=None, **extra_fiels):
#         extra_fiels.setdefault('is_superuser', False)
#         if extra_fiels.get('is_superuser') is not True:
#             raise ValueError('it is not superuser')
#         return self._create_user(username, password, **extra_fiels)

class AdminManager(MainUserManager):
    def create_superuser(self, username, password=None, **extra_fiels):
        extra_fiels.setdefault('is_superuser', True)
        if extra_fiels.get('is_superuser') is not True:
            raise ValueError('it is not superuser')
        return self._create_user(username, password, **extra_fiels)

    def create_stuff(self, username, password=None, **extra_fiels):
        extra_fiels.setdefault('is_superuser', False)
        if extra_fiels.get('is_superuser') is not True:
            raise ValueError('it is not superuser')
        return self._create_user(username, password, **extra_fiels)



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username',max_length=30, unique=True)
    first_name = models.CharField(('first_name'),max_length=30, blank=True)
    last_name = models.CharField(('last_name'),max_length=30, blank=True)
    email = models.EmailField(('email'),max_length=30, blank=True)
    data_joined = models.DateTimeField('data_joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('staff', default=True)
    role = models.SmallIntegerField(choices=USER_ROLES, default=USER_ROLE_ADMIN)

    objects = MainUserManager()

    USERNAME_FIELD = 'username'


class Customer(User):
    birth_date = models.DateField(null=True, blank=True)
    is_staff = False
    role = USER_ROLE_CUSTOMER
    customer_type = models.SmallIntegerField(choices=CUSTOMER_ROLES, default=CUSTOMER_ROLE_ORDINARY)
    objects = CustomerManager()

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class Manager(User):
    avatar = models.ImageField(upload_to=r'C:\Users\User\Desktop\flowerShop\flowerShop\flowerShopBackend\_auth\images\profile_pic', default=r'C:\Users\User\Desktop\flowerShop\flowerShop\flowerShopBackend\_auth\images\profile.png')
    salary = models.FloatField(null=True, blank=True , verbose_name="Salary")
    role = USER_ROLE_MANAGER
    # objects = StaffManager()

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'

class Admin(User):
    avatar = models.ImageField(upload_to=r'C:\Users\User\Desktop\flowerShop\flowerShop\flowerShopBackend\_auth\images\profile_pic', default=r'C:\Users\User\Desktop\flowerShop\flowerShop\flowerShopBackend\_auth\images\profile.png')
    role = USER_ROLE_ADMIN
    objects = AdminManager()

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'
