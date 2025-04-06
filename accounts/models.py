from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    wallet_address = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username
    
    class Meta:
        swappable = 'AUTH_USER_MODEL'
