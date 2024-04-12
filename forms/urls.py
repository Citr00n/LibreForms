from django.urls import include
from django.urls import path
from django.urls import re_path

from .views import *

urlpatterns = [
    path("<uuid:form_id>/", form_view, name="form"),
]
