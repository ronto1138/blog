from blog.groups.models import GroupMember
from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_list_or_404

from django.views import generic
from groups.models import Group, GroupMember
from . import models
# Create your views here.

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ("name","description")
    model = Group
    
class SingleGroup(generic.DetailView):
    model = Group
    
class ListGroup(generic.ListView):
    model = Group