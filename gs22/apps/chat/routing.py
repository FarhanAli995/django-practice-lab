from django.urls import re_path\nfrom apps.chat.consumers import ChatConsumer\n\nwebsocket_urlpatterns = [\n    re_path(r'ws/chat/(?P<room_name>[^/]+)/$', ChatConsumer.as_asgi()),\n]\n
