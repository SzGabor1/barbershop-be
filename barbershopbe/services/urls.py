from django.urls import path
from . import views 

# /api/news/
urlpatterns = [
    path('', views.Service_model_mixin, name = 'service-list'),
    path('employee/', views.service_employee_list_view, name = 'service-employee-list'),
    path('<int:pk>/', views.Service_model_mixin, name = 'service-detail'),
    path('update/<int:pk>/', views.service_update_view ,name = 'service-edit'),
    path('delete/<int:pk>/', views.service_destroy_view),
]

