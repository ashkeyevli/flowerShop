from django.urls import path
from rest_framework import routers

from product.views import CategoryViewSet, FlowerViewSet, CategoryFlowerViewSet
# router = routers.SimpleRouter()
# router.register('<int:pk>/flowers', FlowersViewSet, basename='product')


category_flowers = CategoryFlowerViewSet.as_view({
    'get': 'list'
    # 'post': 'create'
})
router = routers.SimpleRouter()
router.register('flowers', FlowerViewSet ),
router.register('category', CategoryViewSet ),
# router.register('category/<int:pk>/flowers', CategoryFlowerViewSet),
urlpatterns = [
    # # path('category/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('category/<int:pk>/flowers', category_flowers),
    # # path('flowers/<int:pk>', FlowerDetailAPIView.as_view()),
]
urlpatterns += router.urls