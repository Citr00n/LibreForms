from django.shortcuts import render


# Create your views here.

def not_found(req, *args, **kwargs):
    title = 'Страница не найдена'
    return render(req, 'error.html', status=404, context={'title': title})


def server_error(req, *args, **kwargs):
    title = 'Ошибка сервера'
    return render(req, 'error.html', status=500, context={'title': title})


def permission_denied(req, *args, **kwargs):
    title = 'Отказано в доступе'
    return render(req, 'error.html', status=403, context={'title': title})
