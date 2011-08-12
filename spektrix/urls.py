from django.conf.urls.defaults import patterns, include, url

from .views import SpektrixIFrameView


urlpatterns = patterns('',
    url(r'^(?P<page>[^/]+)/$',
        SpektrixIFrameView.as_view(), name='spektrix'),

    url(r'^(?P<page>[^/]+)/(?P<EventId>\d{1,6})/$',
        SpektrixIFrameView.as_view(), name='spektrix'),
)
