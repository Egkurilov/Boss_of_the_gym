from django.db import models

# Create your models here.
class Exercise(models.Model):

    CHOICES = (
        ('STR', 'Силовые'),
        ('CA', 'Кардио'),

    )
    name = models.CharField(max_length=255, default=None)
    type = models.CharField(max_length=300, choices = CHOICES)
    cost = models.CharField(max_length=255, default=None)
    class Meta:
            db_table = "exercises"