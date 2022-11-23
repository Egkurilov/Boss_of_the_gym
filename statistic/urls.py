from django.urls import path
from statistic.views import StatisticView

urlpatterns = [
    path("", StatisticView.as_view()),

]