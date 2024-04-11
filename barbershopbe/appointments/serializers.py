from rest_framework import serializers

from .models import Appointment
from api.serializers import UserPublicSerializer, TimeSlotPublicSerializer
from django.core.validators import EmailValidator
from timeslots.models import TimeSlot


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter timeslots to only include those not related to any appointments
        self.fields['timeslot'].queryset = TimeSlot.objects.filter(appointment__isnull=True)

    class Meta:
        model = Appointment
        fields = [
            'pk',
            'user',
            'email',
            'staff',
            'notification',
            'timeslot'
        ]