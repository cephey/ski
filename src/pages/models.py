#coding:utf-8
from django.db import models


class ServicesText(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=64)
    url_path = models.CharField(verbose_name=u'Url', max_length=32, default='/')
    description = models.TextField(verbose_name=u'Описание', null=True, blank=True)
    image = models.ImageField(verbose_name=u'Картинка', upload_to='pages')
    order = models.SmallIntegerField(verbose_name=u'Порядок')

    class Meta:
        verbose_name = u'Текст под иконкой на главной'
        verbose_name_plural = u'Текст под иконками на главной'
        ordering = ('order',)

    def __unicode__(self):
        return u'{0}'.format(self.title)
