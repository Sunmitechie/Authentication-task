from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.serializers import LoginSerializer as DefaultLoginSerializer

User = get_user_model()
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'phone_number', 'location', 'language_preference']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(DefaultLoginSerializer):
    username = None
    