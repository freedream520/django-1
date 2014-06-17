from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=512)
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True)
