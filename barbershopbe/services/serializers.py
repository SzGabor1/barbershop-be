from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Service
from api.serializers import UserPublicSerializer


class ServiceSerializer(serializers.ModelSerializer):
    employee = UserPublicSerializer(read_only=True)
    class Meta:
        model = Service
        fields = [
            'pk',
            'employee',
            'name',
            'description',
            'price',
            'duration'
        ]


class ServiceCreateSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        queryset = self.fields['employee'].queryset
        self.fields['employee'].queryset = queryset.filter(groups__name='Staff')
        
    class Meta:
        model = Service
        fields = [
            'pk',
            'employee',
            'name',
            'description',
            'price',
            'duration'
        ]
