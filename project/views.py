from django.http import Http404
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.models import User
from administration.models import CarouselImage, Apoiador, BlogPost, Category, Contato, Depoimento
from administration.forms import ApoiadorForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
# classe para renderizar a pagina inicial do site.
class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context["images"] = CarouselImage.objects.filter(ativo=True)[:5]
        context["depoimentos"] = Depoimento.objects.filter(ativo=True)[:5]   
            

        try:
            categoria = Category.objects.get(name='TDAH')      
            context["posttdah"] = BlogPost.objects.filter(category=categoria, destaque_home=True)[:2]

        except ObjectDoesNotExist:
            context["posttdah"] = None
        
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
    
class TDAHBlogView(ListView):
    template_name = 'blog/noticias_tdah.html'
    model = BlogPost
    context_object_name='noticias'
    ordering='-date'
    paginate_by = 9




class TEABlogView(ListView):
    template_name = 'blog/noticias_tea.html'
    model = BlogPost
    context_object_name='noticias'
    ordering='-date'
    paginate_by = 9


    
class NoticiaView(DetailView):
    
    model=BlogPost
    template_name = 'blog/postagem.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        noticia = BlogPost.objects.filter(category=post.category).exclude(id=post.id)[:3]
        context['noticia'] = noticia
        return context
    




class BlogView(TemplateView):
    template_name = 'blog/noticias.html'



class OQueETDAH(TemplateView):
    template_name = 'blog/tdah_infantil.html'
    


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
        num_depoimentos = Depoimento.objects.count()

        context['num_apoiadores'] = num_apoiadores
        context['num_carousel'] = num_carousel
        context['num_blogpost'] = num_blogpost
        context['num_category'] = num_category
        context['num_contatos'] = num_contatos
        context['num_depoimentos'] = num_depoimentos
        return context


# Página de quem somos
class QuemSomos(TemplateView):
    template_name = 'quem-somos.html'

