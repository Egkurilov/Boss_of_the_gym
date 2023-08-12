from django.contrib.auth.decorators import login_required
from django.urls import path

from support.views import SupportView

urlpatterns = [
    path("", login_required(SupportView.as_view)),

]