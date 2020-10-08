from rest_framework import serializers

from .models import Bid
from apps.users.serializers import UserSimpleSerializer
from apps.products.serializers import ProductSerializer


class BidSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Bid
        fields = '__all__'
