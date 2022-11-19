from django.db import models
from user.models import User
from tag.models import ProgrammingLanguageTag, JobTag


# Create your models here.
class Company(models.Model):
    manager = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    name_company = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    established = models.DateField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name_company


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=50)
    experience_required = models.PositiveIntegerField(default=0)
    num_candidate_need = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=255, blank=True, null=True)
    postition = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    end_date = models.DateField()
    salary = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    status = models.PositiveIntegerField(default=0)
    job_types = models.ManyToManyField(JobTag, blank=True, null=True)

    def __str__(self):
        return self.title


class Workflow(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name='workflows')
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
