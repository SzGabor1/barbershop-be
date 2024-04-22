import re
from rest_framework import serializers

class PhoneValidator:
    def __call__(self, value):
        if not re.match(r'^\+?1?\d{9,15}$', value):
            raise serializers.ValidationError("Invalid phone number format")