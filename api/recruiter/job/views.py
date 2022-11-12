from recruiter.serializers import J
from recruiter.models import Job
from django.db.models import Q
from rest_framework import viewsets, permissions, status  # noqa
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.recruiter.serializers import CompanySerializer

