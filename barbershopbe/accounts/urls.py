from django.urls import path
from .views import RegisterView, GetUserView,GetEmployeeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='account_register'),
    path('getUser/', GetUserView.as_view(), name='get_user'),
    path('getemployees/', GetEmployeeView.as_view(), name='get_employees'),
]

