from rest_framework import  generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import News
from .serializers import NewsSerializer
    
from rest_framework import generics, mixins
from .models import News
from .serializers import NewsSerializer
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin, MemberPermissionMixin

class NewsModelMixin(
    MemberPermissionMixin,
    StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        #email= serializer.validated_data.pop('email')
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user= self.request.user, content=content)
        
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     # if not user.is_authenticated:
    #     #     return News.objects.none()
    #     #print(request.user)
    #     return qs.filter(user=request.user)

news_model_mixin = NewsModelMixin.as_view()


# class News_detail_view(generics.RetrieveAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#     lookup_field = 'pk'
    
# news_detail_view = News_detail_view.as_view()


class News_update_view(StaffEditorPermissionMixin,
                       UserQuerySetMixin,
                       generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'pk'
    
    def preform_update(self, serializer):
        instance = serializer.save()
        
        if not instance.content:
            instance.content = instance.title
            instance.save()
        
news_update_view = News_update_view.as_view()


class News_destroy_view(StaffEditorPermissionMixin,
                        UserQuerySetMixin,
                        generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'pk'
    
    def preform_destroy(self, instance):
        super().perform_destroy(instance)
    
news_destroy_view = News_destroy_view.as_view()
'''
class news_list_create_view(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        
news_list_create_view = news_list_create_view.as_view()
'''