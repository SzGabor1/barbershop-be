from django.urls import path
# from .views import api_home
from .views import CustomTokenObtainPairView


urlpatterns = [
    #path('', views.api_home), # localhost:8000/api/
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
]