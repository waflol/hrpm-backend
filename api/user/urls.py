from django.urls import path, include  # noqa
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'user'


urlpatterns = [
    path('register/', views.UserRegisterApiView.as_view(), name='register'),
    path('profile/', views.ManageUserView.as_view(), name='profile')
]
