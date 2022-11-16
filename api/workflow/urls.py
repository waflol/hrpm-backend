from django.urls import path, include  # noqa
from rest_framework.routers import DefaultRouter
from .views import WorkflowViewSet

app_name = 'workflow'
router = DefaultRouter()
router.register(r'workflow', WorkflowViewSet, basename='workflow')

urlpatterns = [
    path('', include(router.urls)),
]
