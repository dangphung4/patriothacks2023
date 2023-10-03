from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

