from rest_framework import serializers
from .models import ProgrammingLanguageTag, JobTag


class ProgrammingLanguageTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguageTag
        fields = '__all__'
        read_only_fields = ['id']


class JobTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTag
        fields = '__all__'
        read_only_fields = ['id']
