from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
# from .views import api_home


urlpatterns = [
    path('', views.api_home), # localhost:8000/api/
    path('auth/', obtain_auth_token), # localhost:8000/api/auth/
]