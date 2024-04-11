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
    timedelta = serializers.IntegerField(write_only=True)  
    
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

        if not user:
            raise serializers.ValidationError('User field cannot be empty')
        
        if start_date > end_date:
            raise serializers.ValidationError('Start date must be before end date')

        return data
    
    def create(self, validated_data):
        user = validated_data.get('user')
        start_date = validated_data.get('start_date')
        end_date = validated_data.get('end_date')
        timedelta_minutes = validated_data.pop('timedelta', 30)
        current_date = start_date
        while current_date < end_date:
            if current_date + timedelta(minutes=timedelta_minutes) == end_date:
                TimeSlot.objects.create(user=user, start_date=current_date, end_date=end_date)
                return {'user': user, 'start_date': current_date, 'end_date': end_date}
            next_date = current_date + timedelta(minutes=timedelta_minutes)
            
            # Check if a TimeSlot with the same start and end dates already exists
            if not TimeSlot.objects.filter(user=user, start_date=current_date, end_date=next_date).exists():
                # Create TimeSlot instance only if it doesn't exist already
                if next_date != end_date or current_date + timedelta(minutes=timedelta_minutes) == end_date:
                    TimeSlot.objects.create(user=user, start_date=current_date, end_date=next_date)
                #   print(f'Created TimeSlot for {user} from {current_date} to {next_date}')
            current_date = next_date
