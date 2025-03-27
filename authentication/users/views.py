from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from dj_rest_auth.views import LoginView, LogoutView, PasswordResetConfirmView, PasswordResetView 
from .serializers import SignupSerializer

user = get_user_model()
class SignupView(generics.CreateAPIView):
    queryset = user.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SignupSerializer

class CustomLoginView(LoginView):
     pass

class CustomLogoutView(LogoutView):
     pass
     
class CustomPasswordResetView(PasswordResetView):
     pass
     
class CustomPasswordResetConfirmView(PasswordResetConfirmView):   
     pass