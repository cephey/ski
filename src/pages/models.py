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


class VeloLevel(models.Model):
    name = models.CharField(verbose_name=u'Уровень подготовки велосипеда', max_length=255)
    image = models.ImageField(verbose_name=u'Картинка', upload_to='velo', blank=True, null=True)
    order = models.SmallIntegerField(verbose_name=u'Порядок', default=0)

    class Meta:
        verbose_name = u'Уровень подготовки велосипеда'
        verbose_name_plural = u'Уровни подготовки велосипедов'
        ordering = ('order',)

    def __unicode__(self):
        return u'{0}'.format(self.name)


class VeloPeroid(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=32)

    class Meta:
        verbose_name = u'Период проката'
        verbose_name_plural = u'Периоды проката'
        ordering = ('name',)

    def __unicode__(self):
        return u'{0}'.format(self.name)


class VeloPrice(models.Model):
    level = models.ForeignKey('pages.VeloLevel', verbose_name=u'Уровень', related_name='velo_price')
    period = models.ForeignKey('pages.VeloPeroid', verbose_name=u'Период')
    price = models.IntegerField(verbose_name=u'Стоимость', default=0)
    holyday = models.IntegerField(verbose_name=u'Стоимость в выходной', blank=True, null=True)

    class Meta:
        verbose_name = u'Цена на велосипед'
        verbose_name_plural = u'Цены на велосипеды'
        ordering = ('level', 'price',)
