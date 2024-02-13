from django.http import Http404
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from administration.models import CarouselImage, Apoiador, BlogPost, Category, Contato
from administration.forms import ApoiadorForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash

# classe para renderizar a pagina inicial do site.
class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = CarouselImage.objects.all()[:5]            
        return context
# Classe para mostrar o perfil do usuário
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
    
# Página de notícias
class BlogView(TemplateView):
    template_name = 'blog/noticias.html'
# Página para mostrar uma postagem.
class NoticiaView(TemplateView):
    template_name = 'blog/postagem.html'
# Classe explicando o que é TDAH
class OQueETDAH(TemplateView):
    template_name = 'blog/tdah_infantil.html'
    
# class ApoioView(TemplateView):
#     template_name = 'apoio/apoio.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["apoiadores"] = Apoiador.objects.all()[:5]            
#         return context
    

# class Painel(LoginRequiredMixin, TemplateView):
#     template_name = 'administration/painel.html'

# Página do administrador
class PainelAdm(LoginRequiredMixin, TemplateView):
    template_name = 'administration/painel_adm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num_apoiadores = Apoiador.objects.count()
        num_blogpost = BlogPost.objects.count()
        num_carousel = CarouselImage.objects.count()
        num_category = Category.objects.count()
        num_contatos = Contato.objects.count()

        context['num_apoiadores'] = num_apoiadores
        context['num_carousel'] = num_carousel
        context['num_blogpost'] = num_blogpost
        context['num_category'] = num_category
        context['num_contatos'] = num_contatos
        return context
# Página de quem somos
class QuemSomos(TemplateView):
    template_name = 'quem-somos.html'

