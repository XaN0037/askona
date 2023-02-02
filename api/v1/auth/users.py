from django.contrib.auth import logout
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.v1.auth.serializer import Userserializer, ChangePasswordSerializer
from api.models import User
from api.v1.auth.servise import BearerAuth
from base.formats import format


class UserView(GenericAPIView):
    serializer_class = Userserializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerAuth,)

    def get(self, request, *args, **kwargs):

        token = request.headers.get("Authorization")
        token = token.split(' ')[1]
        u = Token.objects.filter(key=token).first()
        user = User.objects.filter(pk=u.user_id).first()
        return Response(format(user))

    def put(self, requests, pk, *args, **kwargs):

        data = requests.data
        new = User.objects.get(pk=pk)
        serializer = self.get_serializer(data=data, instance=new, partial=True)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()
        return Response(format(root))


class Logout(GenericAPIView):
    serializer_class = Userserializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerAuth,)

    def get(self, request, *args, **kwargs):
        logout(request)

        return Response({"success": 'logout'})


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerAuth,)
    serializer_class = ChangePasswordSerializer


