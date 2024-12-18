from rest_framework.viewsets import ModelViewSet

from .models import WorkOut, Exercise, MuscleGroup, WorkOut_Exercise


from .serializers import (
    WorkoutSerializer,
    ExerciseSerializer,
    MuscleGroupSerializer,
    WorkOut_ExerciseSerializer,
)


class WorkoutViewSet(ModelViewSet):
    queryset = WorkOut.objects.all()
    serializer_class = WorkoutSerializer


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class MuscleGroupViewSet(ModelViewSet):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer


class WorkOut_ExerciseViewSet(ModelViewSet):
    queryset = WorkOut_Exercise.objects.all()
    serializer_class = WorkOut_ExerciseSerializer
