from django.urls import path, include  # noqa
from . import views
from rest_framework.routers import DefaultRouter
app_name = 'user'
router = DefaultRouter()
router.register(r'users', views.UserListApiViewSet, basename='users')
router.register(r'profile', views.ProfileUserApiViewSet, basename='profile')


urlpatterns = [
    path('', include(router.urls))
]
