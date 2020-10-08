from django.urls import path, include
from rest_framework import routers
from .views import BidViewSet

router = routers.DefaultRouter()
router.register(r'', BidViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
