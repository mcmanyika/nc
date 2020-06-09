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


class UserProfile(models.Model):
    tracker = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    rootid = models.IntegerField()
    title = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    marital_status = models.CharField(
        default='', max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=25, default='', null=True, blank=True)
    member_status = models.CharField(
        max_length=20, default='Student', null=True, blank=True)
    program = models.CharField(
        max_length=30, default='Diploma in Theology', null=True, blank=True)
    program_type = models.CharField(
        max_length=30, default='Diploma', null=True, blank=True)
    sponser = models.CharField(max_length=10, null=True, blank=True)

    country_of_birth = models.CharField(max_length=30, null=True, blank=True)
    nationality = models.CharField(max_length=30, null=True, blank=True)
    passport = models.CharField(max_length=10, null=True, blank=True)
    licence = models.CharField(max_length=10, null=True, blank=True)

    baptised = models.CharField(
        max_length=30, default='Yes', null=True, blank=True)
    church = models.CharField(
        max_length=150, default='', null=True, blank=True)
    how_you_know_us = models.CharField(
        max_length=120, default='Not Applicable', null=True, blank=True)
    access_level = models.IntegerField(default=1, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    image_thumbnail = ImageSpecField(source='avatar',
                                     processors=[ResizeToFill(350, 200)],
                                     format='JPEG',
                                     options={'quality': 60})

    user = models.IntegerField(default=1, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return 'UserProfile {}'.format(self.id)


class Join(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=50, default='00')
    ref_id = models.CharField(max_length=120, default='ABC', unique=True)
    position = models.CharField(max_length=50, default='')
    image = models.FileField(upload_to=upload_location, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("joins:referral_link", kwargs={"email": self.email})

    class Meta:
        ordering = ["-timestamp"]

    class Meta:
        unique_together = ("email", "ref_id",)


class Email(models.Model):
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.email


class t_acct(models.Model):
    g = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )
    rootid = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=g, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    marital_status = models.CharField(default='', max_length=20)
    image = models.FileField(upload_to=upload_location, null=True, blank=True)
    phone = models.CharField(max_length=25, default='', null=True, blank=True)
    zone = models.CharField(max_length=20, default='IOC')
    department = models.CharField(max_length=20, default='')
    member_status = models.CharField(max_length=20, default='Church Member')
    years_in_ministry = models.IntegerField(default='1')
    baptised = models.CharField(max_length=30, default='Yes')
    email = models.EmailField(null=True, blank=True)
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return 't_acct {}'.format(self.id)


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


class t_children(models.Model):
    rootid = models.IntegerField()
    childid = models.IntegerField()
    relationship = models.CharField(max_length=20)

    def __unicode__(self):
        return self.relationship
