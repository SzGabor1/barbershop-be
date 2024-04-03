from rest_framework.routers import DefaultRouter

from news.viewsets import NewsGenericViewSet


router = DefaultRouter()
router.register('news', NewsGenericViewSet, basename='news-detail-v2')

urlpatterns = router.urls
