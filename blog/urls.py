from django.contrib import admin
from django.conf.urls import include, url
from blog.views import *

urlpatterns = [
	
    url(r'^add-article/', add_article, name='add-article'),
    url(r'^add-video/', add_video, name='add-video'),
    url(r'^add-event/', add_event, name='add-event'),
    url(r'^upload-successful/', upload_successful, name='upload-successful'),


    url(r'^article-detail/(?P<id>.*)$', article_detail, name='article-detail'),

    
    
]