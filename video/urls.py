# encoding: utf-8
from django.conf.urls import patterns, url
from views import (
        VideoCreateView, VideoDeleteView, VideoListView,
        )

urlpatterns = patterns('',
    url(r'^new/$', VideoCreateView.as_view(), name='video-new'),
    url(r'^delete/(?P<pk>\d+)$', VideoDeleteView.as_view(), name='video-delete'),
    url(r'^view/$', VideoListView.as_view(), name='video-view'),
)
