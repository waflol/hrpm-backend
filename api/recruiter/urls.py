from django.urls import path, include  # noqa
from rest_framework.routers import DefaultRouter
from recruiter.company import views

app_name = 'recruiter'
router = DefaultRouter()
router.register(r'companylist', views.CompanyListApiView, basename='companylist')
router.register(r'companyregister', views.RegisterCompanyApiView, basename='companyregister')
router.register(r'companyupdate', views.UpdateCompanyApiView, basename='companyupdate')

urlpatterns = [
    path('recruiter/', include(router.urls)),
]
