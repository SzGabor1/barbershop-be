from django.db import models
from django.conf import settings
from timeslots.models import TimeSlot
from services.models import Service

User = settings.AUTH_USER_MODEL

class Appointment(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='app_user')
    service = models.ForeignKey(Service, blank=True, null=True, on_delete=models.SET_NULL) 
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
 #   staff = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='app_staff')
    notification = models.BooleanField(default=True)
    timeslot = models.ForeignKey(TimeSlot, null=True, on_delete=models.SET_NULL)
    token = models.CharField(max_length=100, null=True)
    
