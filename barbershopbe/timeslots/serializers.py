from rest_framework import serializers
from .models import TimeSlot
from api.serializers import UserPublicSerializer
from datetime import timedelta

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        user = UserPublicSerializer(read_only=True)
        model = TimeSlot
        fields = [
            'pk',
            'user',
            'start_date',
            'end_date',
        ]

from datetime import timedelta

class TimeSlotCreateSerializer(serializers.ModelSerializer):
    timedelta = serializers.IntegerField()
    
    class Meta:
        model = TimeSlot
        fields = [
            'user',
            'start_date',
            'end_date',
            'timedelta',
        ]
        
    def validate(self, data):
        user = data.get('user')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        timedelta_minutes = data.get('timedelta', 30)
        
        if not user:
            raise serializers.ValidationError('User field cannot be empty')
        
        if start_date > end_date:
            raise serializers.ValidationError('Start date must be before end date')
        
        time_slots = []
        current_date = start_date
        while current_date < end_date:
            next_date = current_date + timedelta(minutes=timedelta_minutes)  # Use timedelta_minutes
            time_slots.append((current_date, next_date))
            current_date = next_date
        
        for slot_start, slot_end in time_slots:
            TimeSlot.objects.create(user=user, start_date=slot_start, end_date=slot_end)
        
        return data
