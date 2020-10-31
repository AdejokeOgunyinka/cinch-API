from app.action import Action
from daos.user_dao import UsersDAO
from db.serializers.user_serializer import UserSerializer


class VerifyEmailVerify(Action):
    arguments = ['email']

    def perform(self):
        user = UsersDAO.fetch_user_by_email(self.email)
        if user and user.email_verified == False:
            user.email_verified = True
            user.save()
            return UserSerializer(user).data
        else:

            raise Exception('User with the email does not exit')

