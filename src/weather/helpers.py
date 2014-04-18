#coding:utf-8
from datetime import datetime, date
from django.core.cache import cache
from django.conf import settings

from .constants import WEATHER_DICT, WEATHER_FAIL, CITY_DICT, DAY_WEEK
from .exceptions import DayOfWeekException, TemperatureException
from .solar import City, Sun


def get_temperature(condition):
    """
    Return temperature

    """
    try:
        temperature = condition['temp_C']
    except KeyError:
        try:
            min_temperature = condition['tempMinC']
            max_temperature = condition['tempMaxC']
            temperature = u'{0} / {1}'.format(min_temperature, max_temperature)
        except KeyError:
            raise TemperatureException

    return temperature


def get_icon_id(condition, now=False):
    """
    Get api condition and return icon id for widget

    """
    try:
        raw_id = condition['weatherCode']
        id = WEATHER_DICT[raw_id][day_or_night(now)]
    except KeyError:
        return WEATHER_FAIL

    return id


def get_city_name(response, city_name=None):
    """
    Get api response and return russian city name
    If city not in response, return city_name
    """
    try:
        raw_city = response['request'][0]['query']
        city = CITY_DICT[raw_city]
    except (KeyError, IndexError):
        return city_name

    return city


def get_day_of_week(condition):
    """
    Get date in format YYYY-MM-DD and return current day of week

    """
    try:
        raw_date = condition['date']
        _date = datetime.strptime(raw_date, '%Y-%m-%d')
        weekday = DAY_WEEK[_date.weekday()]
    except KeyError:
        raise DayOfWeekException

    return weekday


def day_or_night(now=False):
    """
    Return current time of day(day or night)

    """
    if now:
        solar = get_sunrise_and_sunset()
        if not (solar['sunrise'] < datetime.now() < solar['sunset']):
            return 'night'

    return 'day'


def get_sunrise_and_sunset():
    """
    Return dict with sunrise and sunset time

    """
    data = cache.get('weather_sun', None)

    if not data:
        data = {}
        city = City(
            coordinates=settings.WEATHER_CITY_COORDINATES,
            timeOffset=settings.WEATHER_CITY_TIMEOFFSET)

        proxy = Sun(city)
        proxy.getResult()
        for k, v in proxy.dateRangeSun.items():
            sunrise = datetime.combine(k, (datetime.min + v['Sunrise']['Offical']).time())
            sunset = datetime.combine(k, (datetime.min + v['Sunset']['Offical']).time())

            key = k.strftime('%Y-%m-%d')
            data[key] = {
                'sunrise': sunrise.strftime('%Y-%m-%d %H:%M:%S'),
                'sunset': sunset.strftime('%Y-%m-%d %H:%M:%S')
            }
        cache.set('weather_sun', data, timeout=24 * 60 * 60)

    now = data[date.today().strftime('%Y-%m-%d')]
    return {
        'sunrise': datetime.strptime(now['sunrise'], '%Y-%m-%d %H:%M:%S'),
        'sunset': datetime.strptime(now['sunset'], '%Y-%m-%d %H:%M:%S')
    }
