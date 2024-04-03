from rest_framework import generics

from news.models import News
from news.serializers import NewsSerializer

class SearchListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = News.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results