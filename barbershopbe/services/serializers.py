from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Service
from api.serializers import UserPublicSerializer


class ServiceSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    class Meta:
        model = Service
        fields = [
            'pk',
            'user',
            'name',
            'description',
            'price',
            'duration'
        ]


class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'pk',
            'user',
            'name',
            'description',
            'price',
            'duration'
        ]
