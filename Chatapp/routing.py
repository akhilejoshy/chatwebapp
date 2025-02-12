from django.urls import re_path
from .consumers import ChatConsumer  # Ensure this import is correct

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<interest>\w+)/$", ChatConsumer.as_asgi()),  # Correct pattern
]
