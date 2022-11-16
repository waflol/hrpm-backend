from recruiter.serializers import JobSerializer
from recruiter.models import Job, Company
from django.db.models import Q
from rest_framework import viewsets, permissions, status  # noqa
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class JobListApiView(viewsets.ViewSet, viewsets.generics.ListAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()


class JobCreateApiView(viewsets.ViewSet, viewsets.generics.CreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        if request.user.company:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response('user need create your company before', status=status.HTTP_403_FORBIDDEN)

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)


class JobDeleteApiView(viewsets.ViewSet, viewsets.generics.RetrieveAPIView, viewsets.generics.UpdateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Job.objects.filter(company=self.request.user.company)
