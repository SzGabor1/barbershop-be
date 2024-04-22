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
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,  # Include ListModelMixin
):
    queryset = Appointment.objects.all()
    lookup_field = 'pk'
    
    def get_serializer_class(self):
        return AppointmentSerializer
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)  # Handle list retrieval
        
appointment_model_mixin = AppointmentModelMixin.as_view()



class AppointmentCreateMixin(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
):
    queryset = Appointment.objects.all()
    lookup_field = 'pk'
    
    def get_serializer_class(self):
        return AppointmentCreateSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        # Call the base create method to perform object creation
        return super().create(request, *args, **kwargs)

appointment_create_mixin = AppointmentCreateMixin.as_view()



class AppointmentUpdateView(StaffEditorPermissionMixin,
                        generics.RetrieveUpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCreateSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        return super().update(request, *args, **kwargs)
        
appointment_update_view = AppointmentUpdateView.as_view()

class AppointmentDestroyView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = 'pk'
    
    def preform_destroy(self, instance):
        super().perform_destroy(instance)
        
appointment_destroy_view = AppointmentDestroyView.as_view()