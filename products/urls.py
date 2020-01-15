
from django.conf.urls import include, url
from django.contrib import admin
from products.views import *

urlpatterns = [
    url(r'^$', add_ads, name='add-ads'),
    

]