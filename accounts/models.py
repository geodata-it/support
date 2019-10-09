from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager

Clearance_CHOICES = (
    ('Top_Secret', 'Top_Secret'),
    ('Secret', 'Secret'),
    ('None', "None"))


class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    Clearance = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()
