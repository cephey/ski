#coding: utf-8
import requests
from django.conf import settings
from django.views.generic.base import TemplateView
from pages.models import ServicesText


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        url = '{0}?q={1}&format=json&num_of_days={2}&key={3}'.format(
            settings.WEATHER_API_URL, settings.WEATHER_CITY, 2, settings.WEATHER_API_KEY)

        context['weather'] = None
        try:
            weather = requests.get(url)
            if weather.status_code == 200:
                context['weather'] = weather.json()
        except:
            pass
        # import pdb; pdb.set_trace()

        context['services'] = ServicesText.objects.all()[:4]
        context['address'] = '420095 г. Казань, ул. Горьковское шоссе 49 к2'
        context['phones'] = '8 (843) 225-45-15, 8 917 252 45 15'

        return context
