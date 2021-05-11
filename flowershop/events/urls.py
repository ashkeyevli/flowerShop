from django.urls import path
from events.views import EventViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', EventViewSet)


# urlpatterns = [
#     # path('books/', BookViewSet.as_view({'get': 'list'})),
#     # path('books/<int:pk>/', BookApiView.as_view()),
#     path('authors/<int:pk>/', AuthorApiView.as_view())
# ]

urlpatterns = router.urls