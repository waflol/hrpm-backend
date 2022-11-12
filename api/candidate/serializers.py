from rest_framework import serializers
from .models import CVCandidate


class CVCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CVCandidate
        fields = '__all__'
