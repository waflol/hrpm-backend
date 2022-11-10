from django.shortcuts import render  # noqa
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser


# Create your views here.
# class UserApiViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.filter(is_active=True)
#     serializer_class = UserSerializer

class UserApiViewSet(viewsets.ViewSet,
                     generics.ListAPIView,
                     generics.CreateAPIView,
                     generics.RetrieveAPIView):
    """
    API:
        đăng ký user - generics.CreateAPIView
        lấy thông tin user - generics.RetrieveAPIView
        * lấy danh sách user - generics.ListAPIView
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]
