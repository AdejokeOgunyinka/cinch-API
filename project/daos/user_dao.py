from db.models.user import User
from db.serializers.user_serializer import UserSerializer


class UsersDAO:
    @classmethod
    def fetch_all_users(cls):
        users = User.objects.all()
        return UserSerializer(users, many=True).data

    @classmethod
    def fetch_user_by_email(cls, email):
        users = User.objects.get(email=email)
        return UserSerializer(users, many=False).data

    @classmethod
    def fetch_user_by_otp_code(cls, otp_code):
        users = User.objects.get(otp_code=otp_code)
        return UserSerializer(users, many=False).data

    @classmethod
    def fetch_user_by_username(cls, username):
        users = User.objects.get(username=username)
        return UserSerializer(users, many=False).data

    @classmethod
    def create_user(cls, data):
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            print({"error":serializer.errors})
            return Exception(error=serializer.errors)
