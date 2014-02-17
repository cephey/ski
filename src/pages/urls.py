from django.views.decorators.cache import cache_page
from django.conf.urls import patterns, url

from pages.views import IndexView

urlpatterns = patterns(
    '',
    url(r'^$', cache_page(5 * 60)(IndexView.as_view()), name='index'),
)
