from django.urls import path
from . import views

from django.shortcuts import render

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("artigos/", views.artigos, name="artigos"),
    path("monografias/", views.monografias, name="monografias"),
    path("dissertacao/", views.dissertacao, name="dissertacao"),
    path("tese/", views.tese, name="tese"),
    path("faculdade-direito/", views.faculdade_direito, name="direito"),
    path("faculdade-engenharia/", views.faculdade_engenharia, name="engenharia"),
    path("faculdade-economia/", views.faculdade_economia, name="economia"),
    path("faculdade-gestao/", views.faculdade_gestao, name="gestao"),

  
]