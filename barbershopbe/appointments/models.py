from django.db import models
from django.conf import settings
from timeslots.models import TimeSlot

User = settings.AUTH_USER_MODEL

class Appointment(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='app_user')
    email = models.EmailField(max_length=100, null=True)
    staff = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='app_staff')
    notification = models.BooleanField(default=True)
    timeslot = models.ForeignKey(TimeSlot, null=True, on_delete=models.SET_NULL)
    token = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.timeslot)
