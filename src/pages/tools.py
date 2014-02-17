#coding:utf-8
from django.core.cache import cache as _djcache


def cache(seconds):
    """
    Usage:

    @cache(600)
    def myExpensiveMethod(parm1, parm2, parm3):
        ....
        return expensiveResult

    """
    def decorator(fun):
        def inner_func(*args, **kwargs):
            result = _djcache.get('weather_api')
            if result is None:
                result = fun(*args, **kwargs)
            _djcache.set('weather_api', result, seconds)
            return result
        return inner_func
    return decorator
