from django.http import Http404
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)               
        return context
    
class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/profile.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        update_session_auth_hash(self.request, self.object)
        return response
    
class ContatoView(TemplateView):
    template_name = 'contato/contato.html'


class BlogView(TemplateView):
    template_name = 'blog/noticias.html'

class NoticiaView(TemplateView):
    template_name = 'blog/postagem.html'

class OQueETDAH(TemplateView):
    template_name = 'blog/tdah_infantil.html'
    
class ApoioView(TemplateView):
    template_name = 'apoio/apoio.html'