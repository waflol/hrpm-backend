from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin  # noqa
from django.utils.translation import gettext_lazy as _
from datetime import datetime


# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        extra_fields.setdefault('username', email)
        print(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


def user_avatar_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    dt_string = datetime.now().strftime("%d%m%Y%H%M%S_")
    filename = dt_string + filename
    return 'user_{0}/avatar/{1}'.format(instance.id, filename)


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    is_male = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to=user_avatar_directory_path, blank=True, null=True)  # noqa: E501
    is_recruiter = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'User'

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.first_name + ' ' + self.last_name
