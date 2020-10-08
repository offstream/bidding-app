from rest_framework import serializers

from .models import Product
from apps.bids.models import Bid
from apps.users.serializers import UserSimpleSerializer


class ProductBidsSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer(read_only=True)

    class Meta:
        model = Bid
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer(read_only=True)
    bids = ProductBidsSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
