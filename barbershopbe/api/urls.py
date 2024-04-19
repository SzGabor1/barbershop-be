from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomTokenObtainPairView , CustomTokenRefreshView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import views
# from .views import api_home


urlpatterns = [
    path('auth/', obtain_auth_token),
    #path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('token/', LoginView.as_view(), name='token_obtain_pair'),
]