from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import NotFound
from api.serializers import UserPublicSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import Group


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class GetUserView(generics.RetrieveAPIView):
    authentication_classes = (JWTAuthentication,)

    def get(self, request, *args, **kwargs):
        # Extract JWT token from request headers
        token = request.headers.get('Authorization').split()[1]

        # Decode JWT token to get user ID
        from rest_framework_simplejwt.tokens import AccessToken
        decoded_token = AccessToken(token)
        user_id = decoded_token['user_id']

        # Retrieve user using the user ID
        user = User.objects.get(id=user_id)

        # Serialize user data using UserPublicSerializer
        serializer = UserPublicSerializer(user)

        return Response(serializer.data)
    
class GetEmployeeView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
    
    def get_queryset(self):

        employee_group = Group.objects.get(name='Staff')
        return employee_group.user_set.all()