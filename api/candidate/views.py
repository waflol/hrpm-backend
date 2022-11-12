from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.parsers import MultiPartParser
from user.models import User
from user.serializers import UserSerializer


# Create your views here.
class CandidateProfileApiViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = User.objects.filter(Q(is_active=True) & Q(is_recruiter=False))
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]
