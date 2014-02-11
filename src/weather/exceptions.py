#coding:utf-8


class APIException(Exception):
    pass


class ApiRequestException(APIException):
    pass


class DayOfWeekException(Exception):
    pass


class TemperatureException(Exception):
    pass
