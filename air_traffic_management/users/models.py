from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ('Controller', 'Controller'),
        ('Pilot', 'Pilot'),
        ('Admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.username} ({self.role})"


