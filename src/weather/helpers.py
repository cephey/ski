#coding:utf-8

from datetime import datetime
from .constants import WEATHER_DICT, WEATHER_FAIL, CITY_DICT, DAY_WEEK
from .exceptions import DayOfWeekException, TemperatureException


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
        date = datetime.strptime(raw_date, '%Y-%m-%d')
        weekday = DAY_WEEK[date.weekday()]
    except KeyError:
        raise DayOfWeekException

    return weekday


def day_or_night(now=False):
    """
    Return current time of day(day or night)

    """
    if now:
        # solve
        return 'night'
    else:
        return 'day'
