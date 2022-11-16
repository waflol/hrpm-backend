from django.urls import path, include  # noqa
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'user'
router = DefaultRouter()
router.register(r'', views.UserListApiView, basename='')
router.register(r'register', views.UserRegisterApiView, basename='register')
router.register(r'profile', views.ProfileUserApiView, basename='profile')
router.register(r'userprofile', views.UserProfileApiView, basename='userprofile')



urlpatterns = [
    path('user/', include(router.urls)),
]
