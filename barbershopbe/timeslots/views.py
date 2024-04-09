from rest_framework import generics, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import TimeSlot
from .serializers import TimeSlotSerializer, TimeSlotCreateSerializer
from api.mixins import StaffEditorPermissionMixin, MemberPermissionMixin, UserQuerySetMixin

from api.validators import GroupValidator

class TimeSlotModelMixin(
    MemberPermissionMixin,
    StaffEditorPermissionMixin,
    #UserQuerySetMixin,
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = TimeSlot.objects.all()
    lookup_field = 'pk'
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TimeSlotCreateSerializer
        return TimeSlotSerializer
    
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
        
timeSlot_model_mixin = TimeSlotModelMixin.as_view()

class TimeSlotUpdateView(StaffEditorPermissionMixin,
                        generics.RetrieveUpdateAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotCreateSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Check that the input user belongs to the Worker group
        user = serializer.validated_data.get('user')
        gv = GroupValidator('Staff')
        gv(user)
        
        # If the user input group is valid, proceed with update
        return super().update(request, *args, **kwargs)
        
timeSlot_update_view = TimeSlotUpdateView.as_view()

class TimeSlotDestroyView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    lookup_field = 'pk'
    
    def preform_destroy(self, instance):
        super().perform_destroy(instance)
        
timeSlot_destroy_view = TimeSlotDestroyView.as_view()