import uuid

import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
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
        session_id = uuid.uuid4()
        for question in questions:
            if question.type != "checkbox":
                choices[question] = req.POST.get(str(question.id))
            elif question.type == "checkbox":
                items = []
                i = 0
                for _ in question.choices.all():
                    items.append(req.POST.get(f"{question.id}[{i}]"))
                    i += 1
                choices[question] = items
        if req.user.is_authenticated:
            for question in choices:
                if type(choices[question]) is not list:
                    answer = Answers.objects.create(
                        user=req.user,
                        question=question,
                        choice=choices[question],
                        session_id=session_id,
                    )
                    answer.save()
                else:
                    for choice in choices[question]:
                        answer = Answers.objects.create(
                            user=req.user,
                            question=question,
                            choice=choice,
                            session_id=session_id,
                        )
                        answer.save()
        else:
            for question in choices:
                if question is not list:
                    answer = Answers.objects.create(
                        question=question,
                        choice=choices[question],
                        session_id=session_id,
                    )
                    answer.save()

        if form.only_logged_in:
            if req.user.is_authenticated:
                return render(req, "form.html", context=context)
            else:
                raise PermissionDenied
        return render(req, "form.html", context=context)
