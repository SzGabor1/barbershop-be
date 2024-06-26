from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
class Service(models.Model):
    employee = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)
    duration = models.DecimalField(max_digits=2, decimal_places=1, null=True)

    def __str__(self):
        return str(self.name)
