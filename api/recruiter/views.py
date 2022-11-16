from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Job
from .serializers import JobSerializer, JobDetailSerializer
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
    permission_classes = [IsAuthenticated]

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


# class CompanyViewSet()
