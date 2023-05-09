from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=300, blank=True)
    dob = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
