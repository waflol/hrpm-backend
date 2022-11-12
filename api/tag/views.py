from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import ProgrammingLanguageTag, JobTag
from .serializers import ProgrammingLanguageTagSerializer, JobTagSerializer


# Create your views here.


class ProgrammingLanguageTagListApiView(viewsets.ViewSet, generics.ListAPIView):
    serializer_class = ProgrammingLanguageTagSerializer
    queryset = ProgrammingLanguageTag.objects.all()


class JobTagListApiView(viewsets.ViewSet, generics.ListAPIView):
    serializer_class = JobTagSerializer
    queryset = JobTag.objects.all()
