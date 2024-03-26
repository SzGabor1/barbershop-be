from django.urls import path
from . import views 

# /api/news/
urlpatterns = [
    path('', views.news_model_mixin),
    path('<int:pk>/', views.news_model_mixin),
    path('update/<int:pk>/', views.news_update_view),
    path('delete/<int:pk>/', views.news_destroy_view),
]

