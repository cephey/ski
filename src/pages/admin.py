#coding:utf-8
from django.contrib import admin
from pages.models import ServicesText


class ServicesTextAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url_path', 'order')

admin.site.register(ServicesText, ServicesTextAdmin)
