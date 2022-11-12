from rest_framework import serializers
from .models import ProgrammingLanguageTag, JobTag


class ProgrammingLanguageTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguageTag
        fields = '__all__'


class JobTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTag
        fields = '__all__'
