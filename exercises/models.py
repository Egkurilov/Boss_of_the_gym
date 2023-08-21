from django.db import models
from django_jsonform.models.fields import JSONField
from account.models import User

OPTIONS_SCHEMA = {
    "type": "object",
    "keys": {

        "exercise_one": {
            "$ref": "#/$defs/address"
        },
        "exercise_two": {
            "$ref": "#/$defs/address"
        }
    },
    "$defs": {
        "address": {
            "type": "object",
            "keys": {
                "name": {
                    "type": "string"
                },
                "type": {
                    "type": "string",
                    "title": "Тип",
                    "required": True,
                    "choices": [
                        {"title": "Поле для ввода", "value": "field"},
                        {"title": "Выпадающий список", "value": "select"},
                    ]
                },
                "services": {
                    "type": "list",
                    "title": "Сервисы",
                    "items": {"$ref": "#/$defs/address/services"},
                },

            },
            "services": {
                "type": "object",
                "keys": {
                    "name": {
                        "type": "string",
                        "title": "Название",
                        "required": True,
                    },
                    "value": {
                        "type": "number",
                        "title": "Задержка"
                    },

                },
            }

        }
    }
}


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
    options = JSONField(
        schema=OPTIONS_SCHEMA,
        null=True,
        blank=True,
        verbose_name="Параметры",
    )

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
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "exercise_result"
