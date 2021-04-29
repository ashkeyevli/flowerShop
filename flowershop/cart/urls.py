from django.urls import path
from rest_framework import routers

from cart.views import CartList
urlpatterns = [
    path('/cart', CartList.as_view()),

]