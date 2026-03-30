from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='',  
)