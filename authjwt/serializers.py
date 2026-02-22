
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .services import create_user_with_verification
from .models import EmailVerification
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

class CadasterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        return create_user_with_verification(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()

    def validate(self, attrs):
        email = attrs["email"]
        code = attrs["code"]

        try:
            user = User.objects.get(email=email)
            verification = EmailVerification.objects.get(user=user)
        except:
            raise serializers.ValidationError("Código inválido")

        if verification.code != code:
            raise serializers.ValidationError("Código incorreto")

        user.is_active = True
        user.save()

        verification.is_verified = True
        verification.save()

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email']    = user.email

        return token