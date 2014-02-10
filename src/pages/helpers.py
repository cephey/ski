# import datetime
import requests

from django.conf import settings

from pages.constants import WEATHER_DICT

WEATHER_FAIL = '010'


def get_weather_index(code):
    """
    Return weather picture index

    """
    if not code:
        return WEATHER_FAIL

    if True:
        period = 'day'
    else:
        period = 'night'

    try:
        code_dict = WEATHER_DICT[code]
        return code_dict[period]
    except KeyError:
        return WEATHER_FAIL


def get_weather():
    """
    Return weather api response

    """
    url = '{0}?q={1}&format=json&num_of_days={2}&key={3}'.format(
        settings.WEATHER_API_URL, settings.WEATHER_CITY, 2, settings.WEATHER_API_KEY)

    result = None
    try:
        weather = requests.get(url)
        if weather.status_code == 200:
            result = weather.json()
    except:
        pass

    return result
