from django.conf.urls.defaults import patterns
from views import *

urlpatterns = patterns('',
    (r'^upload/$', UploadVideoView.as_view(), {}, 'video_update'),
    (r'^delete/(?P<pk>\d+)/$', DeleteVideoView.as_view(), {}, 'video_delete'),
    #(r'^view/$', VideoListView.as_view(), name='video-view'),
)
