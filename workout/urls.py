from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ExerciseViewSet, WorkoutViewSet


urlpatterns = []


router = DefaultRouter()
router.register("exercise", ExerciseViewSet)
router.register("workout", WorkoutViewSet)

urlpatterns += router.urls
