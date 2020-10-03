from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Inicio (TemplateView):
    template_name = "index.html"

class Partidos (TemplateView):
    template_name = "Pagina/matches.html"

class Jugadores (TemplateView):
    template_name = "Pagina/players.html"

class Blog (TemplateView):
    template_name = "Pagina/blog.html"

class Contacto (TemplateView):
    template_name = "Pagina/contact.html"
