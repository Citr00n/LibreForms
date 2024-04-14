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
import uuid

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
        session_id = uuid.uuid4()
        for question in questions:
            if question.type == "radio":
                choices[question] = get_object_or_404(Choices,
                                                      id=req.POST.get(
                                                          str(question.id)))
            elif question.type == "text":
                choices[question] = req.POST.get(str(question.id))
            elif question.type == "checkbox":
                choices[question] = req.POST.getlist(str(question.id))
                print(choices[question])
        if req.user.is_authenticated:
            for question in choices:
                if question.type == "radio":
                    answer = UserAnswers.objects.create(question=question,
                                                        choice=choices[question], user=req.user, session_id=session_id)
                elif question.type == "text":
                    answer = UserAnswers.objects.create(question=question,
                                                        text_choice=choices[question], user=req.user, session_id=session_id)
                else:
                    for choice in choices[question]:
                        c = get_object_or_404(Choices, id=choice)
                        print(c)
                        answer = UserAnswers.objects.create(question=question,
                                                            choice=c, user=req.user, session_id=session_id)
                answer.save()
        else:
            for question in choices:
                if question.type == "radio":
                    answer = UserAnswers.objects.create(question=question,
                                                        choice=choices[question], session_id=session_id)
                elif question.type == "text":
                    answer = UserAnswers.objects.create(question=question,
                                                        text_choice=choices[question], session_id=session_id)
                else:
                    for choice in choices[question]:
                        c = get_object_or_404(Choices, id=choice)
                        answer = UserAnswers.objects.create(question=question,
                                                            choice=c, session_id=session_id)
                answer.save()
        if form.only_logged_in:
            if req.user.is_authenticated:
                return render(req, "form.html", context=context)
            else:
                raise PermissionDenied
        return render(req, "form.html", context=context)
