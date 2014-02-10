#coding: utf-8
from django.views.generic.base import TemplateView

from pages.models import ServicesText
from pages.helpers import get_weather_index, get_weather


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['weather'] = get_weather()

        if context['weather']:
            code = context['weather']['data']['current_condition'][0]['weatherCode']
            context['w_index'] = get_weather_index(code)

        context['services'] = ServicesText.objects.all()[:4]
        context['address'] = '420095 г. Казань, ул. Горьковское шоссе 49 к2'
        context['phones'] = '8 (843) 225-45-15, 8 917 252 45 15'

        return context
