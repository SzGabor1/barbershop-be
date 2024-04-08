from rest_framework import generics, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Service
from .serializers import ServiceSerializer, ServiceCreateSerializer
from api.mixins import StaffEditorPermissionMixin, MemberPermissionMixin

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
        user = serializer.validated_data.get('user')
        gv = GroupValidator('Staff')
        gv(user)
        
        # If the user input group is valid, proceed with creation
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()
        
Service_model_mixin = ServiceModelMixin.as_view()
