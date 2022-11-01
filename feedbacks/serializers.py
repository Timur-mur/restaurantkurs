from rest_framework import serializers

from .models import Feedbacks


class FeedbacksListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedbacks
        fields = (
            "id",
            "author",
            "create_date",
            "text",
            "status"
        )


class FeedbacksCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedbacks
        fields = (
            "author",
            "text"
        )
