from django.http import Http404
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)               
        return context
    
class ContatoView(TemplateView):
    template_name = 'contato/contato.html'


class BlogView(TemplateView):
    template_name = 'blog/noticias.html'

class NoticiaView(TemplateView):
    template_name = 'blog/postagem.html'