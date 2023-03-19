from django.contrib.auth.decorators import login_required
from django.urls import path
from gym_app.views import CatalogView, AddView, ExerciseToUser

urlpatterns = [
    path("", login_required(CatalogView.as_view())),
    path("catalog", CatalogView.as_view()),
    path("add", AddView.as_view()),
    path("task/add", ExerciseToUser.as_view()),
]
