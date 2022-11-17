from django.http import Http404
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permissions import IsOwnerOrAdmin
from .models import Job, Workflow
from .serializers import JobSerializer, JobDetailSerializer, WorkflowSerializer
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)


# Create your views here.
@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'job_types',
                OpenApiTypes.STR,
                description='Comma separated list of IDs to filter'
            )
        ]
    )
)
class JobViewSet(viewsets.ModelViewSet):
    """View for manage job APIs."""
    serializer_class = JobDetailSerializer
    queryset = Job.objects.all()

    def get_permissions(self):
        if self.action in ("create", "add_workflow",):
            return [permissions.IsAuthenticated(), ]
        elif self.action in ('update', 'partial_update', 'destroy',):
            return [IsOwnerOrAdmin(), ]
        else:
            return [permissions.AllowAny(), ]

    def _params_to_ints(self, qs):
        """Convert a list of strings to integers. """
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve jobs for authenticated user. """
        job_types = self.request.query_params.get('job_types')
        queryset = self.queryset
        if job_types:
            job_ids = self._params_to_ints(job_types)
            queryset = queryset.filter(job_types__id__in=job_ids)
        return queryset.order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list':
            return JobSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new job"""
        serializer.save(user=self.request.user)

    @action(methods=['get'], detail=True, url_path='workflows')
    @permission_classes([permissions.AllowAny])
    def get_workflow(self, request, pk):
        job = self.get_object()
        workflows = job.worklows
        return Response(WorkflowSerializer(workflows, many=True).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='workflows')
    def add_workflow(self, request, pk):
        try:
            job = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            if request.user == job.user:
                name = request.data.get('name')
                description = request.data.get('description')
                workflow = Workflow.objects.create(job=job, name=name, description=description)
                return Response(WorkflowSerializer(workflow).data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
