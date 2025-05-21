from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("artigos_list/", views.artigo_list, name="artigo_list"),
    path("artigos/<int:pk>/", views.artigo, name="artigos"),
    path("monografia/<int:pk>/", views.monografia_view, name="monografia_view"),
    path("dissertacao/<int:pk>/", views.dissertacao_view, name="dissertacao_view"),
    path("livro/<int:pk>/", views.livro_view, name="livro_view"),
    path("tese/<int:pk>/", views.tese_view, name="tese_view"),
    path("livro/", views.livro, name="livro"),
    path("monografias/", views.monografias, name="monografias"),
    path("dissertacao/", views.dissertacao, name="dissertacao"),
    path("tese/", views.tese, name="tese"),
    path("faculdade-direito/", views.faculdade_direito, name="direito"),
    path("faculdade-engenharia/", views.faculdade_engenharia, name="engenharia"),
    path("faculdade-economia/", views.faculdade_economia, name="economia"),
    path("faculdade-gestao/", views.faculdade_gestao, name="gestao"),
]

    