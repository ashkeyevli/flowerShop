from django.urls import path
from rest_framework import routers

from product.views import categories_view, CategoryDetailAPIView, flowers_view,FlowerDetailAPIView
# router = routers.SimpleRouter()
# router.register('<int:pk>/flowers', FlowersViewSet, basename='product')


# category_flowers = FlowersViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

urlpatterns = [
    path('', categories_view),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('category/<int:pk>/flowers', flowers_view),
    path('flowers/<int:pk>', FlowerDetailAPIView.as_view()),
]
# urlpatterns = router.urls