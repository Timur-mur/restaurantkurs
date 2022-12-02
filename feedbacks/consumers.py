import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from rest_framework import mixins

from .models import Feedbacks

class FeedbacksConsumer(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAsyncAPIConsumer
)