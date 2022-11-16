from recruiter.serializers import CompanySerializer, JobSerializer
from recruiter.models import Company, Job
from django.db.models import Q
from rest_framework import viewsets, permissions, status  # noqa
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user.models import User


class CompanyListApiView(viewsets.ViewSet, viewsets.generics.ListAPIView, viewsets.generics.RetrieveAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        companies = Company.objects.all()
        name = self.request.query_params.get('name')
        location = self.request.query_params.get('location')

        if name:
            companies = companies.filter(Q(name_company__icontains=name))
        if location:
            companies = companies.filter(Q(address__icontains=location))

        return companies

    # @action(methods=['get'], detail=True, url_path='jobs')
    # def get_jobs(self, request, pk):
    #     company = Company.objects.get(id=pk)
    #     jobs = company.jobs.all()
    #     return Response(JobSerializer(jobs, many=True).data, status=status.HTTP_200_OK)


class RegisterCompanyApiView(viewsets.ViewSet, viewsets.generics.CreateAPIView):
    serializer_class = CompanySerializer
    permissions_classes = [IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = User.objects.get(id=request.user.id)
        if user.company:
            return Response('User registered company', status=status.HTTP_400_BAD_REQUEST)
        if user.is_recruiter:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response('User is not recruiter', status=status.HTTP_401_UNAUTHORIZED)

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)


class UpdateCompanyApiView(viewsets.ViewSet, viewsets.generics.UpdateAPIView):
    serializer_class = CompanySerializer
    permissions_classes = [IsAuthenticated, ]

    def get_queryset(self):
        print(self.request.user.id)
        return Company.objects.filter(manager__id=self.request.user.id)

    @action(methods=['get'], detail=False, url_path="current")
    def current_company(self, request):
        print(request.user.id)
        company = Company.objects.get(manager__id=request.user.id)
        return Response(self.serializer_class(company).data, status=status.HTTP_200_OK)
