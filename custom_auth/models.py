from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(unique=True, max_length=30, blank=True, null=True)
    address = models.TextField(max_length=30, blank=True, null=True)
    birth_date = models.DateField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.phone


