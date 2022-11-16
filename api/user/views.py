from django.db.models import Q
from rest_framework import viewsets, permissions, status  # noqa
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser


# Create your views here.
class UserRegisterApiView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
