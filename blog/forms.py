from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from siteInfo.models import *
from django import *
from django.contrib.auth import authenticate, get_user_model, login, logout

from blog.models import *

User = get_user_model()


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = t_subscribe
        fields = [
            'email',
            'mobile',
        ]


class NewsForm(forms.ModelForm):
    class Meta:
        model = t_issue
        fields = [
            'header',
            'description',
            'category',
            'img',
            'user',
        ]


class VideoForm(forms.ModelForm):
    class Meta:
        model = t_video
        fields = [
            'title',
            'thumbnail',
            'url',
            'user',
        ]


class EventForm(forms.ModelForm):
    class Meta:
        model = t_event
        fields = [
            'name',
            'description',
            'category',
            'date',
            'start_time',
            'end_time',
            'address',
            'city',
            'timeline',
            'status',
            'user',
        ]
