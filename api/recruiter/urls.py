from django.urls import path, include  # noqa
from rest_framework.routers import DefaultRouter
from recruiter.job.views import JobViewSet
from recruiter.workflow.views import WorkflowViewSet

app_name = 'recruiter'
router = DefaultRouter()
router.register('jobs', JobViewSet, basename='jobs')
router.register('workflows', WorkflowViewSet, basename='workflows')

urlpatterns = [
    path('', include(router.urls)),
]
