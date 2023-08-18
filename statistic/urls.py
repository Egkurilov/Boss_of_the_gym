from django.contrib.auth.decorators import login_required
from django.urls import path

from statistic.views import StatisticView

urlpatterns = [
    path("", login_required(StatisticView.as_view()), name='statistic'),

]