#coding: utf-8
from django.views.generic.base import TemplateView

from pages.models import ServicesText
from weather.api import WeatherAPI


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        api = WeatherAPI()
        context['weather'] = api.widget()
        context['services'] = ServicesText.objects.all()[:4]

        return context


class VeloView(TemplateView):
    template_name = 'pages/velosiped.html'

    def get_context_data(self, **kwargs):
        context = super(VeloView, self).get_context_data(**kwargs)

        return context


class PalatView(TemplateView):
    template_name = 'pages/palatki.html'

    def get_context_data(self, **kwargs):
        context = super(PalatView, self).get_context_data(**kwargs)

        return context


class SnowView(TemplateView):
    template_name = 'pages/snowboard.html'

    def get_context_data(self, **kwargs):
        context = super(SnowView, self).get_context_data(**kwargs)

        return context


class SkiView(TemplateView):
    template_name = 'pages/mountin_ski.html'

    def get_context_data(self, **kwargs):
        context = super(SkiView, self).get_context_data(**kwargs)

        return context


class UslovView(TemplateView):
    template_name = 'pages/uslovia.html'

    def get_context_data(self, **kwargs):
        context = super(UslovView, self).get_context_data(**kwargs)

        return context


class ContactView(TemplateView):
    template_name = 'pages/contacts.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)

        return context
