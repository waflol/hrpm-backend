from recruiter.serializers import JobSerializer
from recruiter.models import Job
from django.db.models import Q
from rest_framework import viewsets, permissions, status  # noqa
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class JobListApiView(viewsets.ViewSet, viewsets.generics.ListAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
