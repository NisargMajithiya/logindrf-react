from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # override or extend fields
    username = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    user_profileimage = models.ImageField(upload_to="profile/", blank=True, null=True)

    # This tells Django which field is used for login
    USERNAME_FIELD = 'username'
    # These fields will be prompted for when you create a superuser
    REQUIRED_FIELDS = ['email']
