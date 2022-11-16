from rest_framework import serializers
from .models import Workflow, Stepper


class WorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workflow
        fields = '__all__'
        read_only_fields = ['id']


class StepperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stepper
        fields = '__all__'
        read_only_fields = ['id']
