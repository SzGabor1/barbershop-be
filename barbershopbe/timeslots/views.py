from rest_framework import generics, mixins, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import TimeSlot
from .serializers import TimeSlotSerializer, TimeSlotCreateSerializer
from api.mixins import StaffEditorPermissionMixin, MemberPermissionMixin, UserQuerySetMixin
from rest_framework.views import APIView
from api.validators import GroupValidator
from appointments.models import Appointment
class TimeSlotModelMixin(
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
        try:
            start_date = request.data.get('start_date')
            end_date = request.data.get('end_date')
            queryset = self.queryset.filter(start_date__lte=end_date, end_date__gte=start_date)
            print(queryset)
            #return self.list(request, *args, **kwargs)
            return Response(self.get_serializer(queryset, many=True).data)
        except:
            print('No start_date or end_date')
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



class TimeSlotFilteredView(generics.ListAPIView):
    serializer_class = TimeSlotSerializer
    queryset = TimeSlot.objects.all()

    def get_queryset(self):
        start_date_param = self.request.query_params.get('start_date')
        end_date_param = self.request.query_params.get('end_date')
        employee_id = self.request.query_params.get('employee_id')
        
        if start_date_param and end_date_param:
            start_date = start_date_param
            end_date = end_date_param
            queryset = self.queryset.filter(user_id=employee_id, start_date__lte=end_date, end_date__gte=start_date)
            
            
            # return only those timeslots that are not related to any appointments
            queryset = queryset.exclude(appointment__isnull=False)
            
            
            
            return queryset
        else:
            return self.queryset.none()

timeslot_filtered_view = TimeSlotFilteredView.as_view()






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

#Destroy multiple TimeSlot instances in range of start adn end dates
class MultipleTimeSlotDestroyAPIView(StaffEditorPermissionMixin, APIView):

    queryset = TimeSlot.objects.all() 
    def post(self, request, *args, **kwargs):
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        
        self.queryset.filter(start_date__lte=end_date, end_date__gte=start_date).delete()

        
        return Response(status=status.HTTP_204_NO_CONTENT)

multipleTimeSlotDestroyAPIView = MultipleTimeSlotDestroyAPIView.as_view()