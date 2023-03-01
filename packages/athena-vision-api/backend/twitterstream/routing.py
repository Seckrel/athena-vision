from django.urls import re_path
from .consumers import TweetStreamConsumer


websocket_urlpatterns = [
    re_path(r'ws/socket-server/',
            TweetStreamConsumer.as_asgi(), name="tweet_stream")
]
