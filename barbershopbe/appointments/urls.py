from django.urls import path
from . import views 


urlpatterns = [
    path('listall/', views.appointment_model_mixin, name='appointment-list'),
    path('', views.appointment_create_mixin, name='appointment-create'),
    path('<int:pk>/', views.appointment_model_mixin, name='appointment-detail'),
    path('update/<int:pk>/', views.AppointmentUpdateView.as_view(), name='appointment-edit'),
    path('delete/<int:pk>/', views.AppointmentDestroyView.as_view(), name='appointment-delete'),
]