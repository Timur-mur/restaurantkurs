from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Feedbacks
from django.contrib.auth.models import User
from .serializers import FeedbacksListSerializer, FeedbacksCreateSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Feedbacks List': '/feedbacks',
        'Feedbacks Create': '/feeds-create'
    }
    return Response(api_urls)


@api_view(['GET'])
def FeedbacksList(request):
    feeds = Feedbacks.objects.all()
    serializer = FeedbacksListSerializer(feeds, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def FeedbacksCreate(request):
    authorName = User.objects.all()
    dict = {
        "author": authorName.username,
        "text": Feedbacks.text,
    }
    serializer = FeedbacksCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
