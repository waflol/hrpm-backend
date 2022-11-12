from django.db.models import Q
from rest_framework import viewsets, permissions, status  # noqa
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser


# Create your views here.

class UserListApiView(viewsets.ViewSet,
                      generics.ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]


class UserRegisterApiView(viewsets.ViewSet, generics.CreateAPIView):
    serializer_class = UserSerializer


class UserProfileApiView(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]


class ProfileUserApiView(viewsets.ViewSet, generics.UpdateAPIView):
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    @action(methods=['get'], detail=False, url_path="current")
    def current_user(self, request):
        user = User.objects.get(id=request.user.id)
        return Response(self.serializer_class(user).data, status=status.HTTP_200_OK)

    # @action(methods=['put', 'patch'], detail=False, url_path="update")
    # def current_user(self, request):
    #     user = User.objects.get(id=request.user.id)
    #     return Response(self.serializer_class(request.user).data, status=status.HTTP_200_OK)
