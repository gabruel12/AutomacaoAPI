
from django.test import TestCase
import pytest
from rest_framework.exceptions import ValidationError
from ..serializers import CadasterSerializer, LoginSerializer, VerifyEmailSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import EmailVerification
from unittest.mock import patch

@pytest.mark.django_db
@patch("authjwt.serializers.create_user_with_verification")
def teste_cadaster_serializer_create(mock_create):
    user_fake = User(username='gabruel', email='gsr@gmail.com')
    user_fake.set_password("banana")

    mock_create.return_value = user_fake

    data = {
        'username': 'gabruel',
        'email': 'gsr@gmail.com',
        'password': 'banana'
    }

    serializer = CadasterSerializer(data=data)

    assert serializer.is_valid()
    user = serializer.save()

    assert user.username == 'gabruel'
    assert user.email == 'gsr@gmail.com'
    assert user.check_password("banana")

    mock_create.assert_called_once()

@pytest.mark.django_db
def teste_verify_email():
    user = User.objects.create_user(
        username='gabruel',
        email='gsr@gmail.com',
        password='gabriel',
        is_active=False
    )

    verification = EmailVerification.objects.create(
        user=user,
        code='1234',
        is_verified=False
    )

    data = {
        'email': 'gsr@gmail.com',
        'code': '1234'
    }

    serializer = VerifyEmailSerializer(data=data)

    assert serializer.is_valid()
    tokens = serializer.validated_data

    user.refresh_from_db()
    verification.refresh_from_db()

    assert user.is_active is True
    assert verification.is_verified is True
    assert "access" in tokens
    assert "refresh" in tokens

@pytest.mark.django_db
def test_verify_email_wrong_code():
    user = User.objects.create_user(
        username="luiz",
        email="luiz@email.com",
        password="123456",
        is_active=False
    )

    EmailVerification.objects.create(
        user=user,
        code="1234",
        is_verified=False
    )

    data = {
        "email": "luiz@email.com",
        "code": "9999"
    }

    serializer = VerifyEmailSerializer(data=data)

    assert not serializer.is_valid()
    assert "non_field_errors" in serializer.errors