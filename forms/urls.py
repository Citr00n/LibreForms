from django.urls import path, include, re_path
from .views import *
urlpatterns = [
    path('<uuid:form_id>/', form_view, name="form"),
]