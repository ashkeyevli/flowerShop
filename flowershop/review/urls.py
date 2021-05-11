from django.urls import path
from rest_framework import routers

from review.views import reviewAPIView, reviewCreate_view, replyCreate_view


urlpatterns = [
    path('', reviewAPIView.as_view()),
    path('<int:pk>/reply', replyCreate_view),
    path('post', reviewCreate_view),
   ]