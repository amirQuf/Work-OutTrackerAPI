from rest_framework.viewsets import ModelViewSet

from .models import WorkOut, Exercise


from .serializers import WorkoutSerializer, ExerciseSerializer


class WorkoutViewSet(ModelViewSet):
    queryset = WorkOut.objects.all()
    serializer_class = WorkoutSerializer


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
