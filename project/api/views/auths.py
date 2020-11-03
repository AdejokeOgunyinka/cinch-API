from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny


from api.lib.response import Response
from app.auth.register import Register


class AuthsViewSet(ViewSet):
    permission_classes = [AllowAny]

    @action(methods=['post'], detail=False)
    def login(self, request):
        data = dict(sample='User Login Action')
        return Response(data)

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
