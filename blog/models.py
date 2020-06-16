from __future__ import unicode_literals
from django.conf import settings
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from tinymce.models import HTMLField

# Create your models here.


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class t_issue(models.Model):
    header = models.CharField(max_length=100)
    description = HTMLField()
    category = models.CharField(max_length=25, default='policy')
    img = models.FileField(upload_to=upload_location, null=True, blank=True)
    status = models.CharField(max_length=10, default='Active')
    user = models.IntegerField(default=1, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.header


class t_event(models.Model):
    op = (
        ('inverted', 'inverted'),
        ('standard', 'standard')
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=25, default='policy')
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    address = models.CharField(max_length=25, default='')
    city = models.CharField(max_length=25, default='')
    timeline = models.CharField(max_length=10, default='', choices=op)
    status = models.CharField(max_length=10, default='active')
    user = models.IntegerField(default=1, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class t_video(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.FileField(
        upload_to=upload_location, null=True, blank=True)
    url = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=10, default='active')
    user = models.IntegerField(default=1, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title


class t_subscribe(models.Model):
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email
