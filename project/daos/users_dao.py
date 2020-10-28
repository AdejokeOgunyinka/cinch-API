from db.models.user import User
from db.serializers.user_serializer import UserSerializer


class UsersDAO:
    @classmethod
    def fetch_all_users(cls):
        users = User.objects.all()
        return UserSerializer(users, many=True).data

    # @classmethod
    # def update_password(cls, email, password):
    #     user = User.objects.get(email=email)
    #     user['password'] = password
    #     user.save()
    #     return user

