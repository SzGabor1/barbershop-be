from rest_framework import mixins, viewsets

from .models import News

from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'pk'
    
class NewsGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'pk'
    
# news_list_view = NewsGenericViewSet.as_view({'get': 'list'})
# news_detail_view = NewsGenericViewSet.as_view({'get': 'retrieve'})