from django.urls import include, path, re_path

from forms.views import *

from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("", home_view, name="home"),
]
