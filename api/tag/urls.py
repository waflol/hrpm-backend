from django.urls import path, include  # noqa
from rest_framework.routers import DefaultRouter
from .views import ProgrammingLanguageApiView, JobTagViewSet

app_name = 'tag'
router = DefaultRouter()
router.register(r'prolangtag', ProgrammingLanguageApiView, basename='prolangtag')
router.register(r'jobtag', JobTagViewSet, basename='jobtag')

urlpatterns = [
    path('', include(router.urls)),
]
