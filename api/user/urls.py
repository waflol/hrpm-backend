from django.urls import path, include  # noqa
from rest_framework import routers

from .views import UserApiViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserApiViewSet)

app_name = 'user'
urlpatterns = [
    path('', include(router.urls))
]
