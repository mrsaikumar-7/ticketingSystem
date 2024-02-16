from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    """
    Custom user model extending the AbstractUser model.
    """
    is_customer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    def __str__(self):
        """
        String representation of the user.
        """
        return self.username
