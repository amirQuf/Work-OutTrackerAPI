from rest_framework.viewsets import ModelViewSet


from .models import Athlete, Article, UserActivity
from .serializers import ArticleSerializer, UserActivitySerializer, AthleteSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserActivityViewSet(ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
