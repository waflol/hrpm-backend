from django.db.models import Q
from recruiter.models import Job, Workflow
from recruiter.serializers import WorkflowSerializer
from recruiter.permissions import IsOwnerOrAdmin
from rest_framework import viewsets, permissions, status, mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet


class WorkflowViewSet(ReadOnlyModelViewSet):
    serializer_class = WorkflowSerializer
    queryset = Workflow.objects.all()
    permission_classes = [AllowAny, ]
