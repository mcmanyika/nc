from django.contrib import admin
from blog.models import *


# Register your models here.

class IssueModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'header',  'timestamp']
	class Meta:
		model = t_issue
admin.site.register(t_issue, IssueModelAdmin)	

class EventModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'start_time', 'end_time',  'timestamp']
	class Meta:
		model = t_event
admin.site.register(t_event, EventModelAdmin)	

class VideoModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'timestamp']
	class Meta:
		model = t_video
admin.site.register(t_video, VideoModelAdmin)	

class SubscribeModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'email', 'mobile', 'timestamp']
	class Meta:
		model = t_subscribe
admin.site.register(t_subscribe, SubscribeModelAdmin)