from app.action import Action
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class Login(Action):
    arguments = ['data']
    def perform(self):
        email = self.data.get("email")
        password = self.data.get("password")
        if email is None or password is None:
            self.fail(dict(invalid_credential = 'Please provide both email and password'))
        
        user = authenticate(username=email, password=password)

        if not user.email_verified:
            self.fail(dict(verification_failed='Please verify your account'))

        if not user:
            self.fail(dict(invalid_credential='Only registered users can login. Please sign up first.'))
        token, _ = Token.objects.get_or_create(user=user)
        return dict(token=token.key)