from django.urls import path
from . import views 

# /api/news/
urlpatterns = [
    path('', views.timeSlot_model_mixin, name = 'timeSlot-list'),
    path('<int:pk>/', views.timeSlot_model_mixin, name = 'timeSlot-detail'),
    path('update/<int:pk>/', views.timeSlot_update_view ,name = 'timeSlot-edit'),
    path('delete/<int:pk>/', views.timeSlot_destroy_view),
    path('delete/', views.multipleTimeSlotDestroyAPIView),
]

