from django.urls import path

from ordering.views import order_view

urlpatterns = [
    path('create', order_view),

]
# urlpatterns = router.urls