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
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from blog.forms import *
from siteInfo.models import *


# Create your views here.
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def add_article(request):
    dictionary = t_dictionary.objects.all()


    form = NewsForm(request.POST or None, request.FILES or None,)

    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/blog/upload-successful/')
    
    context = {
    	'form' : form,
        'dictionary' : dictionary,
        
    }    

    template = "blog/add_article.html"    

    return render(request, template, context)

def article_detail(request, id):
    instance = get_object_or_404(t_issue, id=id)
    
    context = {
    "header" : instance.header,
    "description" : instance.description,
    "image" : instance.img,
    "category" : instance.category,
    "date" : instance.timestamp,
        
    }    

    template = "blog/article_detail.html"    

    return render(request, template, context)

def add_video(request):


    form = VideoForm(request.POST or None, request.FILES or None,)

    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/blog/upload-successful/')
    
    context = {
        'form' : form,
        
    }    

    template = "blog/add_video.html"    

    return render(request, template, context)

def add_event(request):


    form = EventForm(request.POST or None, request.FILES or None,)

    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/blog/upload-successful/')
    
    context = {
        'form' : form,
        
    }    

    template = "blog/add_event.html"    

    return render(request, template, context)




def upload_successful(request):
    
    context = {
    }    

    template = "blog/upload_successful.html"    

    return render(request, template, context)    