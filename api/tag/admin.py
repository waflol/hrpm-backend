from django.contrib import admin
from .models import JobTag, ProgrammingLanguageTag

# Register your models here.
admin.site.register(JobTag)
admin.site.register(ProgrammingLanguageTag)