from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # User's balance in the app
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        Group,
        related_name='user_groups',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_permissions',
        blank=True,
    )

    def __str__(self):
        return self.username

