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
    return "%s/%s" %(instance.id, filename)

class t_discussion(models.Model):
	header = models.CharField(max_length=50)
	description = models.CharField(max_length=100)
	category = models.CharField(max_length=25, default='policy')
	status = models.CharField(max_length=10, default='Active')
	user = models.IntegerField(default=1, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)

	def __unicode__(self):
	    return self.header
