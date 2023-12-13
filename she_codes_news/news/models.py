from django.db import models
from django.contrib.auth import get_user_model

# User = get_user_model()

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True,blank=True)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE   
        )
    pub_date = models.DateTimeField()
    content = models.TextField()

# New Feature: EditStoryForm
# class EditStoryForm(generic.Model):
#     class Meta:
#         model = NewsStory
#         fields = ['title', 'content']

# Author's View

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

#     def __str__(self):
#         return self.user.username
