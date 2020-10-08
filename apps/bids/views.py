from rest_framework import viewsets

from .models import Bid
from .serializers import BidSerializer


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
