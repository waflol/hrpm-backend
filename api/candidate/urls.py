from django.urls import path, include  # noqa
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'candidate'
router = DefaultRouter()
router.register(r'candidatelist', views.CandidateProfileApiViewSet, basename='candidatelist')

urlpatterns = [
    path('candidate/', include(router.urls)),
]