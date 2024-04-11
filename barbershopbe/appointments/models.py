from django.db import models
from django.conf import settings
from timeslots.models import TimeSlot
User = settings.AUTH_USER_MODEL

class Service(models.Model):
    user = models.ForeignKey(User, blank= True, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(max_length=100, null=True)
    staff = models.ForeignKey(User, blank= True, null=True, on_delete=models.SET_NULL)
    notification = models.BooleanField(default=True)
    timeslot = models.ForeignKey(TimeSlot, null=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return self.timeslot
