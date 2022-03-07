from django.urls import re_path, path
from .views import home, board_topics, new_topic, topic_posts, reply_topic, PostUpdateView

urlpatterns = [
    re_path(r'^$', home, name='home'),
    re_path(r'^(?P<pk>\d+)/$', board_topics, name='board_topics'),
    re_path(r'^(?P<pk>\d+)/new/$', new_topic, name='new_topic'),
    re_path(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', topic_posts, name='topic_posts'),
    re_path(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', reply_topic, name='reply_topic'),
    re_path(r'(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$', PostUpdateView.as_view(),
            name='edit_post'),
]
