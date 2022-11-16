from django.db import models
from recruiter.models import Job
from candidate.models import Candidate


# Create your models here.
class Workflow(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='worklow')
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Stepper(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='step')
    order = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
