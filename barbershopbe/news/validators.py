from rest_framework import serializers
from .models import News
from rest_framework.validators import UniqueValidator

# def validate_title(value):
#         qs = News.objects.filter(title__iexact=value)
#         if qs.exists():
#             raise serializers.ValidationError(f'{value} Is already is a Title')
#         if len(value) < 5:
#             raise serializers.ValidationError('Title must be at least 5 characters long')
#         return value

def validate_title_no_curse(value):
    if "fuck" in value.lower():
        raise serializers.ValidationError(f"{value} is not allowed")
    return value
    
unique_news_title = UniqueValidator(queryset=News.objects.all(), lookup='iexact', message='This title is already in use') 