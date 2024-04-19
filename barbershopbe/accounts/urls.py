from django.urls import path
from .views import RegisterView, GetUser

urlpatterns = [
    path('register/', RegisterView.as_view(), name='account_register'),
    path('getUser/', GetUser.as_view(), name='account_register'),
]

