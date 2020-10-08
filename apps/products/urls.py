from django.urls import path
from .views import ProductViewSet


urlpatterns = [
    path(r'', ProductViewSet.as_view(), name='products')
]
