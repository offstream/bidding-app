from rest_framework import serializers

from .models import Product
from apps.bids.views import BidSerializer


class ProductSerializer(serializers.ModelSerializer):
    bids = BidSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
