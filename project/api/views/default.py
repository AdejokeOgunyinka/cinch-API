from rest_framework.response import Response 
from rest_framework.decorators import api_view


@api_view(['GET'])
def welcome(request):
    return Response(dict(message = 'Welcome to Cinch API'))
