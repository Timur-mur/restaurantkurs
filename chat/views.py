from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.shortcuts import render
from .models import Room, Chat
from .serializers import RoomSerializer, ChatSerializer, ChatPostSerializer


@api_view(['GET'])
def Rooms(request):
    room = Room.objects.all()
    serializer = RoomSerializer(room, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def DialogGet(request):
    room = request.GET.get('room')
    chat = Chat.objects.filter(room=room)
    serializer = ChatSerializer(chat, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DialogPost(request):
    dialog = ChatPostSerializer(data=request.data)
    if dialog.is_valid():
        dialog.save(user=request.user)
        return Response({"status": "Сообщение отправлено"})
    else:
        return Response({"status": "Error"})