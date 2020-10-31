from ..action import Action
from db.serializers.password_serializer import PasswordSerializer


class UpdatePassword(Action):
    """

    """
    arguments = ['user', 'data']

    def perform(self):
        serializer = PasswordSerializer(self.user, data=self.data, many=False, context={
            'user': self.user
        }, partial=True)

        if serializer.is_valid():
            serializer.save()
            return {'data': None}
        else:
            self.fail(serializer.errors)





