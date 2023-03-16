from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from exercises.models import ExerciseList, ExerciseUserResult
from exercises.models import ExerciseType
from exercises.models import ExerciseToUserModel
from django.db.models import Subquery
from django.db.models import OuterRef


class CatalogView(View):
    def get(self, request):
        exercises = (
            ExerciseList.objects.select_related("type")
            .values(
                "type__typecode",
                "type__type",
                "type__exerciselist__name",
                "type_id",
                "type__exerciselist",
            )
            .distinct()
        )

        exercise = {}
        for ex in exercises:
            exercise.setdefault(
                ex["type__typecode"], {"name": ex["type__type"], "data": []}
            )
            exercise[ex["type__typecode"]]["data"].append(ex)

        return render(request, "gym_app/main_page.html", context={"exercise": exercise})


class AddView(View):
    def get(self, request):
        exercises_type = ExerciseType.objects.values()

        user_exercise = {}
        for category in exercises_type:
            user_exercise.setdefault(
                category["id"],
                {
                    "name": category["type"],
                    "typecode": category["typecode"],
                    "data": [],
                },
            )

        exercise_list = (
            ExerciseToUserModel.objects.select_related("exercise")
            .select_related("user")
            .values("exercise_id")
            .annotate(
                exercise_name=Subquery(
                    ExerciseList.objects.values("name").filter(
                        id=OuterRef("exercise_id")
                    )
                )
            )
            .annotate(
                exercise_type=Subquery(
                    ExerciseList.objects.values("type").filter(
                        id=OuterRef("exercise_id")
                    )
                )
            )
            .filter(user_id=request.user.id)
        )

        for ex_list in exercise_list:
            user_exercise[ex_list["exercise_type"]]["data"].append(ex_list)

        return render(
            request,
            "gym_app/add_execises.html",
            context={"user_exercise": user_exercise},
        )

    def post(self, request):
        ExerciseUserResult.objects.create(
            user_id=request.user.id,
            repeat=request.POST["repeat"],
            weight=request.POST["weight"],
            exercise_id=request.POST["exercise-id"],
        )
        print(request.POST)
        return JsonResponse({"result": "success"})


class ExerciseToUser(View):
    def post(self, request):
        ExerciseToUserModel.objects.create(
            exercise_id=request.POST["ex-id"], user_id=request.user.id
        )

        return JsonResponse({"result": "success"})
