# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.utils import timezone
from django.db.models.functions import ExtractDay, ExtractMonth, ExtractYear
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from blog.models import *


# Create your views here.
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]



def index(request):
    events = t_event.objects.all().order_by('-id')[:3]
    videos = t_video.objects.all().order_by('-id')[:3]
    news = t_issue.objects.all().order_by('-id')[:3]


    context = {
        "videos": videos,
        "events": events,
        "news": news,

    }

    template = "videos.html"

    return render(request, template, context)
