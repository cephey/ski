#coding:utf-8
from datetime import date, timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.conf import settings

from weather.solar_event.sun import fills_solar_event_table
from weather.models import SolarEvent
from weather.solar_event.cities import City


class Command(BaseCommand):
    help = "Fills a data SolarEvent time of sunrise and sunset"

    def handle(self, *args, **kwargs):
        now = date.today()
        future = now + timedelta(days=30)

        request = '{0}-{1}'.format(now.strftime('%d.%m.%Y'), future.strftime('%d.%m.%Y'))

        moscow = City(
            coordinates=settings.WEATHER_CITY_COORDINATES,
            timeOffset=settings.WEATHER_CITY_TIMEOFFSET)

        with transaction.atomic():
            SolarEvent.objects.all().delete()
            fills_solar_event_table(request, moscow)
