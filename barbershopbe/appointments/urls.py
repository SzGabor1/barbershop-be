from django.urls import path
from . import views 


urlpatterns = [
    path('', views.appointment_model_mixin, name = 'appointment-list'),
    path('<int:pk>/', views.appointment_model_mixin, name = 'appointment-detail'),
    path('update/<int:pk>/', views.appointment_update_view ,name = 'appointment-edit'),
    path('delete/<int:pk>/', views.appointment_destroy_view),
]

