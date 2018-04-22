from django.conf.urls import url

from .views import (
	users_list, 
	profile_view, 
	send_friend_request, 
	cancel_friend_request,
	accept_friend_request,
	delete_friend_request
	)

urlpatterns = [
    url(r'^$', users_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', profile_view),
    url(r'^friend-request/send/(?P<id>[\w-]+)/$', send_friend_request),
    url(r'^friend-request/cancel/(?P<id>[\w-]+)/$', cancel_friend_request),
    url(r'^friend-request/accept/(?P<id>[\w-]+)/$', accept_friend_request),
    url(r'^friend-request/delete/(?P<id>[\w-]+)/$', delete_friend_request),
]
