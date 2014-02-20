from django.views.decorators.cache import cache_page
from django.conf.urls import patterns, url

from pages.views import IndexView, VeloView, PalatView, SnowView, SkiView, UslovView, ContactView

urlpatterns = patterns(
    '',
    url(r'^$', cache_page(5 * 60)(IndexView.as_view()), name='index'),
    # url(r'^$', IndexView.as_view(), name='index'),

    url(r'^velosipedy/$', VeloView.as_view(), name='velosipedy'),
    url(r'^palatki/$', PalatView.as_view(), name='palatki'),
    url(r'^snoubordy/$', SnowView.as_view(), name='snoubordy'),
    url(r'^gornye_lyzhi/$', SkiView.as_view(), name='gornye_lyzhi'),

    url(r'^uslovia/$', UslovView.as_view(), name='uslovia'),
    url(r'^contacts/$', ContactView.as_view(), name='contacts'),
)
