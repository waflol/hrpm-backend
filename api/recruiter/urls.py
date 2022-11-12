from django.urls import path, include  # noqa
from rest_framework.routers import DefaultRouter
from recruiter.company.views import CompanyListApiView, RegisterCompanyApiView, UpdateCompanyApiView
from recruiter.job.views import JobListApiView

app_name = 'recruiter'
router = DefaultRouter()
router.register(r'companylist', CompanyListApiView, basename='companylist')
router.register(r'companyregister', RegisterCompanyApiView, basename='companyregister')
router.register(r'companyupdate', UpdateCompanyApiView, basename='companyupdate')
router.register(r'joblist', JobListApiView, basename='joblist')


urlpatterns = [
    path('recruiter/', include(router.urls)),
]
