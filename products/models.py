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

class Category(models.Model):
    name = models.CharField(max_length=25)
    order = models.IntegerField(default=1)
    img = models.ImageField()
    status = models.CharField(max_length=10)
    user = models.IntegerField(default=1, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return self.name

class Sub_category(models.Model):
    tracker = models.ForeignKey(Category, on_delete=models.CASCADE)
    root = models.IntegerField(default=1)
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)

    def __unicode__(self):
        return self.name    


class Products(models.Model):
    tracker = models.ForeignKey(Category, on_delete=models.CASCADE, default='1')
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=25)
    description = models.CharField(max_length=400, default='Description')
    img = models.FileField(upload_to=upload_location, null=True, blank=True)
    # image_thumbnail = ImageSpecField(source='avatar',
    #     processors=[ResizeToFill(350, 200)],
    #     format='JPEG',
    #     options={'quality': 60})

    user = models.IntegerField(default=1, null=True, blank=True)
    date = models.DateField(auto_now_add = True, auto_now=False)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return self.name 

     