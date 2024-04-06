from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('', views.home_view, name='home'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup_view, name='signup')
]