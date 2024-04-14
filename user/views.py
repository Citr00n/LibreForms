from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.shortcuts import redirect
from django.shortcuts import render

from . import forms

# Create your views here.


def login_view(req):
    """

    :param req:

    """
    if req.user.is_authenticated is True:
        return redirect("index")

    elif req.method == "GET":
        form = forms.UserForm()
        return render(req,
                      "login.html",
                      context={
                          "title": "Вход",
                          "form": form
                      })

    elif req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect("home")
        else:
            raise PermissionDenied


def home_view(req):
    """

    :param req:

    """
    if req.user.is_authenticated is True:
        return render(req,
                      "userhome.html",
                      context={"title": req.user.username})
    else:
        return redirect("login")


def logout_view(req):
    """

    :param req:

    """
    if req.user.is_authenticated is True:
        if req.method == "GET":
            return render(req, "logout.html", context={"title": "Выход"})
        elif req.method == "POST":
            logout(req)
            return redirect("login")
    else:
        return redirect("login")


def signup_view(req):
    """

    :param req:

    """
    if req.user.is_authenticated is not True:
        if req.method == "GET":
            form = forms.UserForm()
            return render(req,
                          "signup.html",
                          context={
                              "title": "Регистрация",
                              "form": form
                          })

        elif req.method == "POST":
            if not list(User.objects.all()):
                superuser = True
            else:
                superuser = False

            try:
                user = User.objects.create_user(
                    username=req.POST["username"],
                    password=req.POST["password"],
                    is_staff=True, is_superuser=superuser,
                )
                user.save()
                group = Group.objects.get(name="default")
                user.groups.add(group)
                login(req, user)
            except IntegrityError:
                raise PermissionDenied
    return redirect("home")
