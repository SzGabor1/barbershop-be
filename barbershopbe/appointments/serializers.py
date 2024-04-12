from rest_framework import serializers

from .models import Appointment
from api.serializers import UserPublicSerializer, TimeSlotPublicSerializer
from django.core.validators import EmailValidator
from timeslots.models import TimeSlot
from django.contrib.auth.models import Group
from django.utils.crypto import get_random_string

class AppointmentSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    staff = UserPublicSerializer(read_only=True)
    timeslot = TimeSlotPublicSerializer(read_only=True)
    class Meta:
        model = Appointment
        fields = [
            'pk',
            'user',
            'email',
            'staff',
            'notification',
            'timeslot'
            #DELETE URL FOR CANCEL APPOINTMENT
        ]
        
        


class AppointmentCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator(message="Invalid email format")])
    token = serializers.CharField(read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter staff members to only include those in the "Staff" group
        staff_group = Group.objects.get(name='Staff')  # Assuming 'Staff' is the name of your staff group
        self.fields['staff'].queryset = staff_group.user_set.all()

        # Filter timeslots to only include those not related to any appointments
        self.fields['timeslot'].queryset = TimeSlot.objects.filter(appointment__isnull=True)

    def create(self, validated_data):
        # Generate token
        validated_data['token'] = get_random_string(length=32)  # Generate a random token
        return super().create(validated_data)

    class Meta:
        model = Appointment
        fields = [
            'pk',
            'user',
            'email',
            'staff',
            'notification',
            'timeslot',
            'token'
        ]