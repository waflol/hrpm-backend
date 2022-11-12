from datetime import datetime

from django.db import models

from recruiter.models import Job
from user.models import User


# Create your models here.
def user_cv_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    dt_string = datetime.now().strftime("%d%m%Y%H%M%S_")
    filename = dt_string + filename
    return 'user_{0}/resumes/{1}'.format(instance.id, filename)


class CVCandidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cv_file = models.FileField(upload_to=user_cv_directory_path)
    applied = models.ManyToManyField(Job, blank=True)

    def __str__(self):
        return self.user.email
