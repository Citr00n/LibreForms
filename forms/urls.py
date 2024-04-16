from django.urls import include
from django.urls import path
from django.urls import re_path

from .views import *

urlpatterns = [
    path("<uuid:form_id>/", form_view, name="form"),
    path("<uuid:form_id>/analytics", analytics_view, name="analytics"),
    path("<uuid:form_id>/export/", exports_view, name="exports"),
    path("<uuid:form_id>/export/<uuid:question_id>", export_view, name="question_export"),
]
