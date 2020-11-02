from app.action import Action
from django.contrib.auth import get_user_model
from db.models.user import User
from db.serializers.user_serializer import UserSerializer

class VerifyEmailVerify(Action):
    arguments =['email']

    def perform(self):
        user = get_user_model().objects.get(email=self.email)
        if user and user.email_verified == False:
            user.email_verified = True
            user.save()
            return UserSerializer(user).data
        else:

            raise Exception('User with the email is already verified')