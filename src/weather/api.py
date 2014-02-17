#coding:utf-8
import requests
from django.conf import settings
# from django.core.cache import cache
# from django.utils.decorators import method_decorator
from pages.tools import cache
# from django.views.decorators.cache import cache_page

from .exceptions import APIException, ApiRequestException, DayOfWeekException, TemperatureException
from .helpers import get_icon_id, get_city_name, get_day_of_week, get_temperature


class WeatherAPI(object):
    """
    Weather proxy

    """
    def __init__(self):

        self.days = 4

        self.url = '{0}?q={1}&format=json&num_of_days={2}&key={3}'.format(
            settings.WEATHER_API_URL, settings.WEATHER_CITY, self.days, settings.WEATHER_API_KEY)

    def _api_response(self):
        """
        Get weather from API

        """
        try:
            weather = requests.get(self.url)
            if weather.status_code == 200:
                data = weather.json().get('data', {})
            else:
                raise ApiRequestException
        except:
            raise APIException

        return data

    @cache(5 * 60)
    def __call__(self):
        """
        Weather data for widget

        """
        result = {}
        try:
            data = self._api_response()
        except APIException:
            return None

        try:
            current_condition = data['current_condition'][0]
            result['city_name'] = get_city_name(data, settings.WEATHER_CITY_TRANS)
            result['icon_id'] = get_icon_id(current_condition, True)
            result['temperature'] = get_temperature(current_condition)
        except (KeyError, IndexError, TemperatureException):
            return None

        result['forecast'] = []
        if 'weather' in data:
            for day_condition in data['weather']:
                buf = {}
                try:
                    buf['day_of_week'] = get_day_of_week(day_condition)
                    buf['icon_id'] = get_icon_id(day_condition)
                    buf['temperature'] = get_temperature(day_condition)
                except (DayOfWeekException, TemperatureException):
                    continue
                result['forecast'].append(buf)

        return result
