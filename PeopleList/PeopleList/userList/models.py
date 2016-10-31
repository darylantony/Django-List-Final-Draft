from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Skill(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.name



class User(models.Model):
    name = models.CharField(max_length=30)
    user_skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name
