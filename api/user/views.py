from django.shortcuts import render  # noqa
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


# Create your views here.
class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
