#coding:utf-8
from django.core.management.base import BaseCommand
from django.core.cache import cache
from django.conf import settings


class Command(BaseCommand):
    help = "Drop all cache key"

    def handle(self, *args, **kwargs):
        for key in settings.ALL_CACHE_KEY:
            cache.set(key, None)
            print('drop ``{0}``'.format(key))