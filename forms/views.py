import uuid
from collections import Counter

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from plotly.subplots import make_subplots

from .models import *
from .plots import *

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
                        if choice is not None:
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


def analytics_view(req, form_id, *args, **kwargs):
    form = Forms.objects.get(id=form_id)
    charts = {}
    for question in form.questions.all():
        a = []
        for item in Answers.objects.filter(question=question).values("choice"):
            a.append(item["choice"])
        occ = Counter(a)
        choice = []
        count = []
        for k, v in occ.items():
            choice.append(k)
            count.append(v)
        print(f"{choice}//{count}")
        chart = plot_piechart(names=choice, values=count, title=f"{question.question}")
        charts[question.id] = chart

    return render(req, "analytics.html", context={"charts": charts, "form": form})
