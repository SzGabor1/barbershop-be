from django.urls import path
from . import views 

# /api/news/
urlpatterns = [
    path('', views.Service_model_mixin, name = 'service-list'),
    path('<int:pk>/', views.Service_model_mixin, name = 'service-detail'),
    # path('update/<int:pk>/', views.news_update_view ,name = 'service-edit'),
    # path('delete/<int:pk>/', views.news_destroy_view),
]

