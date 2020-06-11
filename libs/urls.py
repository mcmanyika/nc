from django.contrib import admin
from django.conf.urls import include, url
from libs.views import *

urlpatterns = [

    url(r'^home/', index, name='home'),
    url(r'^add-ad/', add_ads, name='add-ad'),
    url(r'^ad-detail/(?P<id>.*)$', ad_detail, name='ad-detail'),
    url(r'^list-by-category/(?P<id>.*)$', category, name='list-by-category'),
    url(r'^master/', master, name='master'),
    url(r'^detail/', detail, name='detail'),

    url(r'^videos/', video, name='videos'),
    url(r'^issues/', issues, name='issues'),
    url(r'^base-b/', base_b, name='base-b'),
    url(r'^base-c/', base_c, name='base-c'),
    url(r'^base-d/', base_d, name='base-d'),
    url(r'^base-e/', base_e, name='base-e'),
    url(r'^base-f/', base_f, name='base-f'),






]
