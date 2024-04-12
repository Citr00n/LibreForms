from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

def form_view(req, form_id, *args, **kwargs):
    form = get_object_or_404(Forms, id=form_id)
    questions = form.questions.all()
    q = {}
    n = len(list(questions))
    for i in questions:
        q[i.id] = list(i.choices.all())
    print(q)


    context = {
        'title': form.title,
        'description': form.description,
        'confirmation_msg': form.confirmationMsg,
        'id': form.id,
    }

    return render(req, 'form.html', context=context)
