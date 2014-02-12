#coding:utf-8
from django.db import models


class SolarEvent(models.Model):
    date = models.DateField()
    sunrise = models.DateTimeField(verbose_name=u'Время восхода')
    sunset = models.DateTimeField(verbose_name=u'Время Заката')

    class Meta:
        verbose_name = u'Время восхода и заката солнца'
        verbose_name_plural = u'Время восхода и заката солнца'

    def __unicode__(self):
        return u'{0}'.format(self.date)
