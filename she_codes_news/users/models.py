# from django.db import models
#Author's View
# from django.db import models
# from django.contrib.auth import get_user_model
# User = get_user_model()
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    profile_url = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True)
    def __str__(self):
        return self.username

#Author's view
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

#     def __str__(self):
#         return self.user.username