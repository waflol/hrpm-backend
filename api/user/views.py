from django.shortcuts import render  # noqa
from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser


# Create your views here.
# class UserApiViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.filter(is_active=True)
#     serializer_class = UserSerializer

class UserListApiViewSet(viewsets.ViewSet,
                         generics.CreateAPIView,
                         generics.ListAPIView):
    """
    API:
        đăng ký user - generics.CreateAPIView
        lấy thông tin user - generics.RetrieveAPIView
        * lấy danh sách user - generics.ListAPIView
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]


class ProfileUserApiViewSet(viewsets.ViewSet, generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]
    lookup_field = "id"

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
