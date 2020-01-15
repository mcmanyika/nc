from django.contrib import admin
from .models import *


# Register your models here.

class DiscussionModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'header',  'timestamp']
	class Meta:
		model = t_discussion
admin.site.register(t_discussion, DiscussionModelAdmin)		