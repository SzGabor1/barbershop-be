from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class BlobModel(models.Model):
    employee = models.ForeignKey(User, default=1, blank=True, null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=100)
    blob_data = models.BinaryField()

    def __str__(self):
        return self.type
