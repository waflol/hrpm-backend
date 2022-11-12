from django.urls import path, include  # noqa
from rest_framework.routers import DefaultRouter
from .views import ProgrammingLanguageTagListApiView, JobTagListApiView

app_name = 'tag'
router = DefaultRouter()
router.register(r'prolangtag', ProgrammingLanguageTagListApiView, basename='prolangtag')
router.register(r'jobtag', JobTagListApiView, basename='jobtag')

urlpatterns = [
    path('tag/', include(router.urls)),
]
