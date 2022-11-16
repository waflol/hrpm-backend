from django.shortcuts import render
from rest_framework import viewsets, generics, mixins
from rest_framework.permissions import IsAuthenticated

from .models import ProgrammingLanguageTag, JobTag
from .serializers import ProgrammingLanguageTagSerializer, JobTagSerializer


# Create your views here.


class ProgrammingLanguageApiView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProgrammingLanguageTagSerializer
    queryset = ProgrammingLanguageTag.objects.all()


class JobTagViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Manage Job tags in the database"""
    serializer_class = JobTagSerializer
    queryset = JobTag.objects.all()
