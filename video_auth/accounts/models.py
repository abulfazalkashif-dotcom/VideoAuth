from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class videoUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/')
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.video_file.name}"




















# # Create your models here.

# class UserAccount(models.Model):
#     username = models.CharField(max_length=150)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     date_created = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.username

