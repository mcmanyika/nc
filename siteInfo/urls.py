from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
   url(r'^insert-zone/', insert_zone, name='insert-zone'),
   url(r'^add-event/', add_event, name='add-event'),

    #url(r'^loggedin/', loggedin, name='loggedin'),
]