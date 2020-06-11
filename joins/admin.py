from django.contrib import admin

from .models import *


class EmailModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'timestamp']

    class Meta:
        model = Email


admin.site.register(Email, EmailModelAdmin)


class AttriModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'department', 'level', 'status', 'timestamp']

    class Meta:
        model = t_user_attribute


admin.site.register(t_user_attribute, AttriModelAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'rootid', 'name', 'category']

    class Meta:
        model = t_group


admin.site.register(t_group, GroupAdmin)
