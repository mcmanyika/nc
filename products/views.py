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
from products.models import *
from products.forms import *

# Create your views here.

def add_ads(request):

	category = Category.objects.all().order_by('order')
	products = Products.objects.all().order_by('-id')


	form = AdvertForm(request.POST or None, request.FILES or None)
	if form.is_valid():
	    f = form.save(commit=False)
	    f.save()
	    messages.success(request, "Saved")
	    return HttpResponseRedirect('/')
    
	context = {
		"categories" : category,
		"products" : products,
		"form" : form,
	}    

	template = "products/add_ads.html"    

	return render(request, template, context)

