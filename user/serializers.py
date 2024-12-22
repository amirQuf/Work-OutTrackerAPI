from rest_framework import serializers
from .models import Athlete, Article, UserActivity


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = (
            "id",
            "username",
            "email",
            "status",
            "bio",
            "age",
            "weight",
            "height",
            "level",
            "picture",
            "strick",
        )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "id",
            "author",
            "title",
            "content",
            "created",
            "updated",
            "is_published",
        )


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = ("id", "author", "exercise", "time")
