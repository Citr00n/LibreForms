from django.urls import include, path, re_path

from .views import *

urlpatterns = [
    path("<uuid:form_id>/", form_view, name="form"),
]
