from datetime import datetime
from django.db import models


# Create your models here.
def user_cv_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    dt_string = datetime.now().strftime("%d%m%Y%H%M%S_")
    filename = dt_string + filename
    return 'user_{0}/resumes/{1}'.format(instance.id, filename)


class Candidate(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    cv = models.FileField(upload_to=user_cv_directory_path, null=True, blank=True)

    def __str__(self):
        return self.email
