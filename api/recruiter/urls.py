from django.urls import path, include  # noqa
from rest_framework.routers import DefaultRouter
from .views import JobViewSet


app_name = 'recruiter'
router = DefaultRouter()
router.register('jobs', JobViewSet, basename='jobs')


urlpatterns = [
    path('', include(router.urls)),
]
