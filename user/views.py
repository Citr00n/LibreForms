from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.shortcuts import redirect
from django.shortcuts import render

from forms.models import Forms
from . import forms

# Create your views here.


def login_view(req):
    """

    :param req:

    """
    if req.user.is_authenticated is True:
        return redirect("home")

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


def logout_view(req):
    """

    :param req:

    """
    if req.user.is_authenticated is True:
        if req.method == "GET":
            return render(req, "logout.html", context={"title": "Выход"})
        elif req.method == "POST" and req.path != "/admin/logout":
            logout(req)
            return redirect("index")
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
                default = Group.objects.create(name="default")
                print(default)
                default.save()
                for i in range(25, 37, 1):
                    print(i)
                    default.permissions.add(Permission.objects.get(id=i))
            else:
                superuser = False
            try:
                user = User.objects.create_user(
                    username=req.POST["username"],
                    password=req.POST["password"],
                    is_staff=True,
                    is_superuser=superuser,
                )
                user.save()
                group = Group.objects.get(name="default")
                user.groups.add(group)
                login(req, user)
            except IntegrityError:
                raise PermissionDenied
    return redirect("home")


def home_view(req):
    """

    :param req:

    """
    if req.user.is_authenticated is True:
        user_forms = Forms.objects.filter(creator=req.user)
        return render(req,
                      "userhome.html",
                      context={
                          "title": req.user.username,
                          "forms": user_forms
                      })
    else:
        return redirect("login")
