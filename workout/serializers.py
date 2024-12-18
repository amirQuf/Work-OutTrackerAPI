from rest_framework import serializers

from .models import Exercise, WorkOut, WorkOut_Exercise, MuscleGroup


class MuscleParentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = [
            "id",
            "name",
            "is_active",
            "created",
            "modified",
        ]


class MuscleGroupSerializer(serializers.ModelSerializer):
    Parent_muscle = MuscleParentGroupSerializer()

    class Meta:
        model = MuscleGroup
        fields = [
            "id",
            "name",
            "Parent_muscle",
            "is_active",
            "created",
            "modified",
        ]


class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            "id",
            "name",
            "is_private",
            "is_active",
            "planed",
            "created",
            "modified",
            "status",
            "workout_exercises",
        ]
        model = WorkOut


class ExerciseSerializer(serializers.ModelSerializer):
    muscle_group = MuscleGroupSerializer()

    class Meta:
        model = Exercise
        fields = [
            "id",
            "name",
            "muscle_group",
            "is_active",
            "created",
            "modified",
            "description",
            "category",
            "difficulty",
            "is_active",
        ]


class WorkOut_ExerciseSerializer(serializers.ModelSerializer):
    WorkOut = WorkoutSerializer()
    Exercise = ExerciseSerializer()

    class Meta:
        fields = [
            "id",
            "WorkOut",
            "Exercise",
            "rep",
            "sets",
            "created",
        ]
        model = WorkOut_Exercise
