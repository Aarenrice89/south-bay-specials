from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        return token


class RegisterNewUserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if User.objects.filter(username=attrs["email"], email=attrs["email"]).exists():
            raise serializers.ValidationError(f"User with email: {attrs['email']} already exists")
        return attrs

    def create(self, validated_data) -> AbstractUser:
        user_obj = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            username=validated_data["email"],
            password=validated_data["password"],
        )
        return user_obj
