from django.db import models
from account.models import User


# Create your models here.
class ExerciseType(models.Model):
    type = models.CharField(max_length=255, default=None)
    typecode = models.CharField(max_length=255, default=None)

    class Meta:
        db_table = "exercise_type"

    def __str__(self):
        return self.type


class ExerciseList(models.Model):
    type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default=None)
    cost = models.CharField(max_length=255, default=None)

    class Meta:
        db_table = "exercise_list"


class ExerciseToUserModel(models.Model):
    exercise = models.ForeignKey(ExerciseList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "exercise_user"


class ExerciseUserResult(models.Model):
    exercise = models.ForeignKey(ExerciseList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.CharField(max_length=255, default=None)
    repeat = models.CharField(max_length=255, default=None)

    class Meta:
        db_table = "exercise_result"
