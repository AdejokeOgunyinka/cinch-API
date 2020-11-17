from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from app.action import Action
from lib.lower_strip import strip_and_lower


class Login(Action):
    arguments = ['data']

    def perform(self):
        email = strip_and_lower(self.data.get('email', ''))
        password = self.data.get('password', '')

        if email is None or password is None:
            self.fail(dict(invalid_credential='Please provide both email and password'))
        
        user = authenticate(username=email, password=password)

        if not user:
            self.fail(dict(invalid_credential='Please ensure that your email and password are correct'))

        if not user.email_verified:
            self.fail(dict(verification_failed='Please verify your account'))
            
        token, _ = Token.objects.get_or_create(user=user)
        return dict(token=token.key)
