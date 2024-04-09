from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL #auth.User


class TimeSlot(models.Model):
    user = models.ForeignKey(User, default=1, null = True, on_delete=models.SET_NULL)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def get_absolute_endpont(self):
        return f'/api/timeslot/{self.pk}/'