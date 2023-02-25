from django.db import models


# Create your models here.
class ExerciseType(models.Model):
    type = models.CharField(max_length=255, default=None)
    typecode = models.CharField(max_length=255, default=None)

    class Meta:
        db_table = "exercise_type"


class ExerciseList(models.Model):
    type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default=None)
    cost = models.CharField(max_length=255, default=None)

    class Meta:
        db_table = "exercise_list"


