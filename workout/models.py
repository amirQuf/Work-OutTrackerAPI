from django.db import models


class MuscleGroup(models.Model):
    name = models.CharField(max_length=200, unique=True)
    Parent_muscle = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):

    CATEGORY_CHOICES = (
        ("E", "endurance"),
        ("S", "strength"),
        ("B", "balance"),
        ("F", "flexibility"),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=1, default="E", choices=CATEGORY_CHOICES)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)
    difficulty = models.PositiveSmallIntegerField(default=5)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class WorkOut(models.Model):
    STATUS_CHOICE = (
        ("C", "Created"),
        ("P", "planned"),
        ("D", "Done"),
        ("I", "In Progress"),
    )

    name = models.CharField(max_length=200)
    is_private = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    planed = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default="C", choices=STATUS_CHOICE)

    def __str__(self):
        return self.name


class WorkOut_Exercise(models.Model):
    WorkOut = models.ForeignKey(WorkOut, on_delete=models.CASCADE)
    Exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    rep = models.PositiveSmallIntegerField(default=10)
    sets = models.PositiveSmallIntegerField(default=3)
