from rest_framework import serializers

from .models import Exercise, WorkOut, WorkOut_Exercise, MuscleGroup


class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = "__all__"


class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = WorkOut


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["name"]


class WorkOut_ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = WorkOut_Exercise
