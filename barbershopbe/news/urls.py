from django.urls import path
from . import views 

# /api/news/
urlpatterns = [
    path('', views.news_model_mixin, name = 'news-list'),
    path('<int:pk>/', views.news_model_mixin, name = 'news-detail'),
    path('update/<int:pk>/', views.news_update_view ,name = 'news-edit'),
    path('delete/<int:pk>/', views.news_destroy_view),
]

