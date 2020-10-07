from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'is_admin')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        is_admin = validated_data.pop('is_admin')
        user = get_user_model().objects.create_user(**validated_data)
        user.is_admin = is_admin
        user.save()
        return user


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
