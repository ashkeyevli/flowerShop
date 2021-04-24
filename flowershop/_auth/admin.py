from django.contrib import admin

# Register your models here.
from _auth.models import  User, Manager, Admin, Customer

admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Admin)
admin.site.register(Customer)