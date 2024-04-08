from rest_framework import serializers
from django.contrib.auth.models import Group

class GroupValidator:
    def __init__(self, group_name):
        self.group_name = group_name

    def __call__(self, user):
        group = Group.objects.get(name=self.group_name)
        if not group.user_set.filter(id=user.id).exists():
            raise serializers.ValidationError(f"User does not belong to the group '{self.group_name}'")
