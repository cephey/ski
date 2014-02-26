#coding:utf-8
from django.contrib import admin
from pages.models import ServicesText, VeloPrice, VeloLevel, VeloPeroid


class ServicesTextAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url_path', 'order')


class VeloPriceAdmin(admin.ModelAdmin):
    list_display = ('level', 'period', 'price', 'holyday')


admin.site.register(ServicesText, ServicesTextAdmin)
admin.site.register(VeloPrice, VeloPriceAdmin)
admin.site.register(VeloLevel)
admin.site.register(VeloPeroid)
