"""
URL configuration for LibreForms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView
from user.views import *
from utils.views import *

urlpatterns = [
    path("admin/logout/", logout_view, name="logout"),
    path("admin/", admin.site.urls),
    path("form/", include("forms.urls")),
    path("user/", include("user.urls")),
    path("", index, name="index"),
    path("__debug__/", include("debug_toolbar.urls")),
]

handler404 = "utils.views.not_found"
handler500 = "utils.views.server_error"
handler403 = "utils.views.permission_denied"
