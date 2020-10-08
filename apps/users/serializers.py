from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('last_name', 'first_name')


class UserSerializer(serializers.ModelSerializer):
    bids = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'is_admin',
                  'profile', 'products', 'bids')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        is_admin = validated_data.pop('is_admin')
        user = get_user_model().objects.create_user(**validated_data)
        user.is_admin = is_admin
        user.save()
        return user
