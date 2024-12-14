from django.db import models


from django.contrib.auth.models import AbstractUser


class Athlete(AbstractUser):
    TRAINER = 1
    MEMBER = 2
    ADMIN = 3

    ROLES = (
        (TRAINER, "trainer"),
        (MEMBER, "member"),
        (ADMIN, "admin"),
    )
    email = models.EmailField(unique=True)
    status = models.SmallIntegerField(choices=ROLES, default=MEMBER)
    bio = models.CharField(max_length=200, null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    weight = models.PositiveSmallIntegerField(default=80)
    height = models.PositiveSmallIntegerField(default=150)
    level = models.PositiveSmallIntegerField(default=0)
    status = models.SmallIntegerField(choices=ROLES, default=MEMBER)
    picture = models.ImageField(upload_to="profile_pic", null=True, blank=True)
    strick = models.IntegerField(default=0)


class Article(models.Model):
    author = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


from workout.models import Exercise
from django.utils.timezone import now


class UserActivity(models.Model):
    author = models.ForeignKey(
        Athlete, null=True, blank=True, on_delete=models.SET_NULL
    )
    exercise = models.ForeignKey(
        Exercise, null=True, blank=True, on_delete=models.SET_NULL
    )
    time = models.DateTimeField(default=now)
