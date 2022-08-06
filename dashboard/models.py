from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = 'aaa'
