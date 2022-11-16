from jsonschema._validators import required
from rest_framework import serializers
from .models import Company, Job
from tag.serializers import JobTagSerializer
from tag.models import JobTag


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name_company', 'address', 'phone_number', 'email', 'description', 'established', 'website']
        read_only_fields = ['id']


class JobSerializer(serializers.ModelSerializer):
    """Serializer for job"""
    job_types = JobTagSerializer(many=True, required=False)

    class Meta:
        model = Job
        fields = ['id', 'title', 'experience_required', 'num_candidate_need', 'postition', 'end_date', 'salary', 'job_types']
        read_only_fields = ['id']

    def _get_or_create_jobtags(self, job_types, job):
        """Handle getting or creating job types as needed"""
        for tag in job_types:
            tag_obj, created = JobTag.objects.get_or_create(
                **tag
            )
            job.job_types.add(tag_obj)

    def create(self, validated_data):
        """Create a job. """
        job_types = validated_data.pop('job_types', [])
        job = Job.objects.create(**validated_data)
        self._get_or_create_jobtags(job_types, job)
        return job

    def update(self, instance, validated_data):
        """Update a job"""
        job_types = validated_data.pop('job_types', None)
        if job_types is not None:
            instance.job_types.clear()
            self._get_or_create_jobtags(job_types, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class JobDetailSerializer(JobSerializer):
    """Serializer for job detail view. """

    class Meta(JobSerializer.Meta):
        fields = JobSerializer.Meta.fields + ['description', 'address', ]
