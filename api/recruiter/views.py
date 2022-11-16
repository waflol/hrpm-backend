from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Job
from .serializers import JobSerializer, JobDetailSerializer


# Create your views here.
class JobViewSet(viewsets.ModelViewSet):
    """View for manage job APIs."""
    serializer_class = JobDetailSerializer
    queryset = Job.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve jobs for authenticated user. """
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list':
            return JobSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new job"""
        serializer.save(user=self.request.user)


