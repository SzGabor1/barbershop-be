from rest_framework import generics, mixins, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Appointment
from .serializers import AppointmentSerializer, AppointmentCreateSerializer
from api.mixins import StaffEditorPermissionMixin, MemberPermissionMixin, UserQuerySetMixin
from rest_framework.views import APIView
from api.validators import GroupValidator

class AppointmentModelMixin(
    MemberPermissionMixin,
    StaffEditorPermissionMixin,
    #UserQuerySetMixin,
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Appointment.objects.all()
    lookup_field = 'pk'
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AppointmentCreateSerializer
        return AppointmentSerializer
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
    # If neccesarry email could be equal to the user email
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()
        
appointment_model_mixin = AppointmentModelMixin.as_view()