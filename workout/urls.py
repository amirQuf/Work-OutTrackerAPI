from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ExerciseViewSet, WorkoutViewSet, MuscleGroupViewSet


urlpatterns = []


router = DefaultRouter()
router.register("exercise", ExerciseViewSet)
router.register("workout", WorkoutViewSet)
router.register("muscles", MuscleGroupViewSet)

urlpatterns += router.urls
