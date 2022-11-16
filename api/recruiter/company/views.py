from recruiter.serializers import CompanySerializer
from recruiter.models import Company
from django.db.models import Q
from rest_framework import viewsets, permissions, status  # noqa
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


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


class RegisterCompanyApiView(viewsets.ViewSet, viewsets.generics.CreateAPIView):
    serializer_class = CompanySerializer
    permissions_classes = [IsAuthenticated, ]

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
