# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(null=True, blank=True, max_length=100)
    state = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return '{} {}'.format(self.country, self.state)