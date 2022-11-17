from django.contrib import admin
from .models import Job, Company, Workflow, Stepper

# Register your models here.

admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Workflow)
admin.site.register(Stepper)