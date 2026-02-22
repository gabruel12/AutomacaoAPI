
import secrets
import string
from django.contrib.auth import get_user_model
from .models import EmailVerification
from .tasks import email_verificacao

User = get_user_model()

def generate_verification_code(size=4):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(size))

def create_user_with_verification(username, email, password):
    user = User.objects.create_user(
        usernmae  = username,
        email     = email,
        password  = password,
        is_active = False
    )

    code = generate_verification_code()

    EmailVerification.objects.update_or_create(
        user     = user,
        defaults = {"code": code, "is_verified": False}
    )

    email_verificacao.delay(user.username, user.email, code)

    return user