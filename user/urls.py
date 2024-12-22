from rest_framework.routers import DefaultRouter

from .views import UserActivityViewSet, ArticleViewSet

router = DefaultRouter()

router.register("article", ArticleViewSet)
router.register("user_activity", UserActivityViewSet)

urlpatterns = router.urls
