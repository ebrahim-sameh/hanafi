from django.db import models
from django.contrib.auth.models import User,AbstractUser
from PIL import Image


class User(AbstractUser):
   gender = models.BooleanField(default=True)
   phone = models.CharField(max_length=11,default='')
   Country = models.CharField(max_length=11,default='')
   City = models.CharField(max_length=11,default='')
   email = models.EmailField()
   student = models.BooleanField(default='false')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'
