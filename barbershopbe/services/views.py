from rest_framework import generics, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Service
from .serializers import ServiceSerializer, ServiceCreateSerializer
from api.mixins import StaffEditorPermissionMixin, MemberPermissionMixin, UserQuerySetMixin

from api.validators import GroupValidator

class ServiceModelMixin(
    MemberPermissionMixin,
    StaffEditorPermissionMixin,
    #UserQuerySetMixin,
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Service.objects.all()
    lookup_field = 'pk'
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ServiceCreateSerializer
        return ServiceSerializer
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        #Check that the input user belongs to the Worker group
        employee = serializer.validated_data.get('employee')
        gv = GroupValidator('Staff')
        gv(employee)
        
        # If the user input group is valid, proceed with creation
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()
        
Service_model_mixin = ServiceModelMixin.as_view()


class ServiceEmployeeListView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        employee_id = self.request.query_params.get('employee_id')
        if employee_id:
            queryset = Service.objects.filter(employee_id=employee_id)
            return queryset
        else:
            return Service.objects.none()
    
    
service_employee_list_view = ServiceEmployeeListView.as_view()

class ServiceUpdateView(StaffEditorPermissionMixin,
                        generics.RetrieveUpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceCreateSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Check that the input user belongs to the Worker group
        employee = serializer.validated_data.get('employee')
        gv = GroupValidator('Staff')
        gv(employee)
        
        # If the user input group is valid, proceed with update
        return super().update(request, *args, **kwargs)
        
service_update_view = ServiceUpdateView.as_view()

class ServiceDestroyView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'pk'
    
    def preform_destroy(self, instance):
        super().perform_destroy(instance)
        
service_destroy_view = ServiceDestroyView.as_view()