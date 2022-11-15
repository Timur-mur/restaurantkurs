from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Room, Chat


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializer(serializers.ModelSerializer):

    admin = UserSerializer()
    clients = UserSerializer()

    class Meta:
        model = Room
        fields = ("admin", "clients", "date")


class ChatSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Chat
        fields = ("user", "text", "date")


class ChatPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ("room", "text", )