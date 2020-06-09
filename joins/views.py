#import requests
import json
import math
from django.db import connection
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, Http404
from .forms import EmailForm, JoinForm, JoinForm2, UserRegisterForm
from .models import Join
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Count
from joins.forms import User
from django.contrib.auth.decorators import login_required
from siteInfo.models import *
from joins.forms import *
import uuid
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from products.models import *
from siteInfo.models import *
from libs.models import *

# Create your views here.

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def register_view(request):
    dictionary = t_dictionary.objects.all().order_by('order')

    form = UserRegisterForm(request.POST or None)
    form2 = JoinForm2(request.POST or None)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dash/')
            else:
                messages.success(request, "Enter correct username or password")
 
    if request.method == 'POST':
        passchange = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            passchange_user = user.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('change_password')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        passchange = PasswordChangeForm(request.user)            

      

    context = {
        "dictionary" : dictionary,
        "form" : form,
        "form2" : form2,
        "passchange" : passchange,
        

    }
    return render(request, "signin.html", context)

def register(request):
    instance = get_object_or_404(t_dictionary, category='title')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user-img')
    else:
        form = SignUpForm()

    context = {
        "form": form,
        "image" : instance.image,
        }    
    return render(request, 'register.html', context)   

def logout(request):
    logout(request)
    return HttpResponseRedirect('/libs/base/')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user-img')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_img(request):
    headings = t_dictionary.objects.all().order_by('id')
    rw = t_dictionary.objects.all().order_by("name")
    img_form = AvatarForm(request.POST or None, request.FILES or None)
    if img_form.is_valid():
        f = img_form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return redirect('signup-confirmation')

    context = {
        "headings" : headings,
        "rw" : rw,
        "img_form" : img_form,
    }    
    template = 'user_img.html'
    return render(request, template, context)

def signup_confirmation(request):
    
    return render(request, 'signup_confirmation.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('change_password')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
}) 






