import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from plotly.subplots import make_subplots

from .models import *

# Create your views here.


def form_view(req, form_id, *args, **kwargs):
    """

    :param req: param form_id:
    :param form_id: param *args:
    :param *args: 
    :param **kwargs: 

    """
    form = get_object_or_404(Forms, id=form_id)
    questions = form.questions.all()
    nq = len(list(questions))
    nc = {}
    for i in questions:
        nc[i] = len(list(i.choices.all()))
    if req.method == "GET":

        context = {
            "title": form.title,
            "description": form.description,
            "confirmation_msg": form.confirmationMsg,
            "id": form.id,
            "questions": questions,
            "form": form,
            "choices": nc,
            "confirm": False,
        }
        if form.only_logged_in:
            if req.user.is_authenticated:
                return render(req, "form.html", context=context)
            else:
                raise PermissionDenied
        return render(req, "form.html", context=context)

    elif req.method == "POST":
        context = {
            "title": form.title,
            "description": form.confirmationMsg,
            "id": form.id,
            "form": form,
            "confirm": True,
        }
        choices = {}
        for question in questions:
            choices[question] = get_object_or_404(
                Choices, id=req.POST.get(str(question.id))
            )
        if req.user.is_authenticated:
            for question in choices:
                answer = UserAnswers.objects.create(
                    user=req.user, question=question, choice=choices[question]
                )
                answer.save()
        else:
            for question in choices:
                answer = UserAnswers.objects.create(
                    question=question, choice=choices[question]
                )
                answer.save()
        if form.only_logged_in:
            if req.user.is_authenticated:
                return render(req, "form.html", context=context)
            else:
                raise PermissionDenied
        return render(req, "form.html", context=context)
