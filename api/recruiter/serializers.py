from rest_framework import serializers
from .models import Company, Job
from tag.serializers import ProgrammingLanguageTagSerializer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name_company', 'address', 'phone_number', 'email', 'description', 'established', 'website']


class JobSerializer(serializers.ModelSerializer):
    """Serializer for job"""

    class Meta:
        model = Job
        fields = ['id', 'title', 'experience_required', 'num_candidate_need',  'postition', 'end_date', 'salary']
        read_only_fields = ['id']


class JobDetailSerializer(JobSerializer):
    """Serializer for job detail view. """
    class Meta(JobSerializer.Meta):
        fields = JobSerializer.Meta.fields + ['description', 'address', ]
