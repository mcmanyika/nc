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
from blog.forms import *


# Create your views here.
def landing(request):

    form = SubscribeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/base/')

    context = {
        "form": form,

    }

    template = "newsletter.html"

    return render(request, template, context)


def index(request):
    events = t_event.objects.all().order_by('-id')[:3]
    videos = t_video.objects.all().order_by('-id')[:3]
    news = t_issue.objects.all().order_by('-id')[:3]

    form = SubscribeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        # return HttpResponseRedirect('/')

    context = {
        "videos": videos,
        "events": events,
        "news": news,
        "form": form,

    }

    template = "index.html"

    return render(request, template, context)


def add_ads(request):

    context = {

    }

    template = "add_ads.html"

    return render(request, template, context)


def dash(request):

    context = {

    }

    template = "dashboard.html"

    return render(request, template, context)


def donate(request):

    context = {

    }

    template = "donate.html"

    return render(request, template, context)


def index2(request):
    category = Category.objects.all().order_by('order')
    subcategory = Sub_category.objects.all().order_by('id')
    products = Products.objects.all().order_by('-id')[:4]

    context = {
        "categories": category,
        "subcategory": subcategory,
        "products": products,

    }

    template = "index.html"

    return render(request, template, context)


def category(request, id):
    category = Category.objects.all().order_by('order')
    products = Products.objects.filter(tracker=id).order_by('-id')
    context = {
        "categories": category,
        "products": products,

    }

    template = "category.html"

    return render(request, template, context)


def ad_detail(request, id):
    category = Category.objects.all().order_by('order')
    instance = get_object_or_404(Products, id=id)

    context = {
        "categories": category,
        "name": instance.name,
        "price": instance.price,
        "description": instance.description,
        "image": instance.img,
        "date": instance.date,

    }

    template = "ad_detail.html"

    return render(request, template, context)


def master(request):

    context = {

    }

    template = "master.html"

    return render(request, template, context)


def detail(request):

    context = {

    }

    template = "detail.html"

    return render(request, template, context)


def video(request):

    videos = t_video.objects.all().order_by('-id')

    context = {

        "videos": videos,

    }

    template = "videos.html"

    return render(request, template, context)


def issues(request):

    issues = t_issue.objects.all().order_by('-id')

    context = {
        "issues": issues,

    }

    template = "issues.html"

    return render(request, template, context)
