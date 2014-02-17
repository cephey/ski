#coding: utf-8
from django.views.generic.base import TemplateView

from pages.models import ServicesText
from weather.api import WeatherAPI


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['weather'] = WeatherAPI()()

        context['services'] = ServicesText.objects.all()[:4]
        context['address'] = '420095 г. Казань, ул. Горьковское шоссе 49 к2'
        context['phones'] = '8 (843) 225-45-15, 8 917 252 45 15'

        return context
