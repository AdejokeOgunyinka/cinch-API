from ..action import Action
from db.serializers.password_serializer import PasswordSerializer


class UpdatePassword(Action):
    """

    """
    arguments = ['user', 'data']

    def perform(self):
        cur_user = self.user
        data = self.data
        user = PasswordSerializer(cur_user, data=data, many=False, context={
            "user": cur_user
        }, partial=True)

        if user.is_valid():
            user_info = user.save()
            data = {
                "username":user_info.username,
                "email":user_info.email
            }
            return data
        else:
            raise Exception("Error")





