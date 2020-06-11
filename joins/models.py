from __future__ import unicode_literals
from django.conf import settings
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms

# Create your models here.


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Email(models.Model):
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.email


class t_user_attribute(models.Model):
    op = (
         ('Yes', 'Yes'),
         ('No', 'No')
    )
    root = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return 't_user_attribute {}'.format(self.id)


class t_group(models.Model):
    rootid = models.IntegerField()
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return 't_group {}'.format(self.id)
