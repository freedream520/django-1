from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(User)
    info = models.CharField(max_length=256)
    link = models.URLField()
    viewed = models.BooleanField(default=False)
