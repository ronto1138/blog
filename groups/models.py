from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

# Create your models here.
class GroupMember(models.Model):
    group = model.ForeignKey(Group,related_name='membership',on_delete=models.CASCADE)
    user = model.FeringKey(User,related_name='user_grpups', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ('group','user')