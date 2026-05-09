from django.db import models

from django.db import models 
from django.contrib.auth import get_user_model

User = get_user_model()


class Permission(models.Model): 
    key = models.CharField(max_length=128, unique=True) 
    name = models.CharField(max_length=255) 
    description = models.TextField(blank=True)
    
    class Meta: 
        ordering = ["key"] 
        def __str__(self): 
            return self.key 


class Group(models.Model): 
    key = models.CharField(max_length=128, unique=True) 
    name = models.CharField(max_length=255) 
    permissions = models.ManyToManyField(Permission, related_name="groups", blank=True) 
    

class UserAccess(models.Model): 
    groups = models.ManyToManyField( Group, related_name="user_access", blank=True) 
    permissions = models.ManyToManyField(Permission, related_name="user_access", blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    user_access = models.OneToOneField(UserAccess, on_delete=models.SET_NULL, null=True, blank=True, related_name="profile")
