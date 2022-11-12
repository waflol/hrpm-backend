from django.db.models import Q
from rest_framework import viewsets, permissions, status  # noqa
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser


# Create your views here.

class UserListApiViewSet(viewsets.ViewSet,
                         generics.CreateAPIView,
                         generics.ListAPIView):
    """
    Đăng ký và lấy thông tin tất cả User
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]


class ProfileUserApiViewSet(viewsets.ViewSet, generics.RetrieveUpdateAPIView):
    """
        User bắt buộc phải đăng nhập mới có thể update và vào profile của mình
    """
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    @action(methods=['get'], detail=False, url_path="current")
    def current_user(self, request):
        return Response(self.serializer_class(request.user).data, status=status.HTTP_200_OK)


class CandidateProfileApiViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = User.objects.filter(Q(is_active=True) & Q(is_recruiter=False))
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]
