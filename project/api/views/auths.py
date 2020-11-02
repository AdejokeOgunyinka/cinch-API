from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny


from api.lib.response import Response
from app.auth.register import Register
from rest_framework.permissions import AllowAny
from rest_framework import status
from app.auth.login import Login


class AuthsViewSet(ViewSet):
    permission_classes = [AllowAny]
    @action(methods=['post'], detail=False)
    def login(self, request):
        '''Generates a token based on the email and password passed in as parameters.
        e.g: {'email': 'enter_email_here', 'password': 'your_password'}'''
        login_details = Login.call(data=request.POST)
        if login_details.failed:
            return Response(
                errors=login_details.error.value,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            data=login_details.value,
            status=status.HTTP_200_OK
        )

    @action(methods=['post'], detail=False)
    def register(self, request):
        artist = Register.call(data=request.data)
        
        if artist.failed:
            return Response(
                errors=artist.error.value,
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            data=artist.value, 
            status=status.HTTP_201_CREATED
        )
