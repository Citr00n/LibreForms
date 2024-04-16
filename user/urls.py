from django.urls import include
from django.urls import path
from django.urls import re_path

from . import views
from forms.views import *

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("", home_view, name="home"),
]
