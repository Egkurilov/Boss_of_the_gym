from django.contrib.auth.decorators import login_required
from django.urls import path
from gym_app.views import CatalogView, AddView, ExerciseToUser

urlpatterns = [
    path("", login_required(CatalogView.as_view())),
    path("catalog", login_required(CatalogView.as_view()), name='catalog'),
    path("add", login_required(AddView.as_view())),
    path("task/add", login_required(ExerciseToUser.as_view())),
]
