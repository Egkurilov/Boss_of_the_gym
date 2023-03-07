from django.shortcuts import render
from django.views import View
from exercises.models import ExerciseList
from exercises.models import ExerciseToUserModel


class CatalogView(View):
    def get(self, request):
        exercises = ExerciseList.objects.select_related('type').values("type__typecode", "type__type",
                                                                       "type__exerciselist__name", "type_id").distinct()
        exercise = {}
        for ex in exercises:
            exercise.setdefault(ex['type__typecode'], {'name': ex['type__type'], 'data': []})
            exercise[ex['type__typecode']]['data'].append(ex)
        return render(request, 'gym_app/main_page.html', context={'exercise': exercise})


class AddView(View):
    def get(self, request):
        return render(request, 'gym_app/add_execises.html')


class ExerciseToUser(View):
    def post(self, request):
        ExerciseToUserModel.objects.create(exercise_id=request.POST['ex-id'], user_id=request.user.id)


        return render(request, 'gym_app/add_execises.html')
