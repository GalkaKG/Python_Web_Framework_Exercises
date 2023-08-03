from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from todos_rest_workshop.accounts.serialaizers import RegisterUserSerializer


class ApiLoginUserView(ObtainAuthToken):
    pass


class ApiRegisterUserView(CreateAPIView):
    serializer_class = RegisterUserSerializer


class ApiLogoutUserView(APIView):
    def post(self, request, *args, **kwargs):
        return self.__perform_logout(request)

    def get(self, request, *args, **kwargs):
        return self.__perform_logout(request)

    @staticmethod
    def __perform_logout(request):
        request.user.auth_token.delete()
        return Response({
            'message': 'user logged out'
        })
