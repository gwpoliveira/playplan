from django.db.models.query import QuerySet
from django.http import Http404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.models import User
from administration.models import CarouselImage, Apoiador, BlogPost, Category, Contato, Depoimento, Inscricao
from administration.forms import ApoiadorForm, ContatoForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import render



# classe para renderizar a pagina inicial do site.
class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        num_carousel = CarouselImage.objects.filter(ativo=True).count()
        context['num_carousel'] = num_carousel        
        context["images"] = CarouselImage.objects.filter(ativo=True)[:5]
        context["depoimentos"] = Depoimento.objects.filter(ativo=True)[:5] 
        num_depoimentos = Depoimento.objects.filter(ativo=True).count()
        context['num_depoimentos'] = num_depoimentos    
            

        try:
            categoria = Category.objects.get(name='TDAH')      
            context["posttdah"] = BlogPost.objects.filter(category=categoria, destaque_home=True).order_by('-date')[:2].select_related('category')

        except ObjectDoesNotExist:
            context["posttdah"] = None
        
    
        try:
            categoria = Category.objects.get(name='TEA')
            context["posttea"] = BlogPost.objects.filter(category=categoria, destaque_home=True).order_by('-date')[:2].select_related('category')

        except ObjectDoesNotExist:
            context["posttea"] = None

        return context

    
# View responsável por carregar a página de Contato
class ContatoCreateView(CreateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'contato/contato.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Mensagem enviada com sucesso!")
        return reverse('home')


# View responsável por carregar a página Apoiador    
class ApoiadorCreateListView(CreateView, ListView):
    model = Apoiador
    form_class = ApoiadorForm
    template_name = 'apoio/apoio.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["apoiadores"] = Apoiador.objects.filter(visivel=True)[:5]            
        return context

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Obrigado por apoiar nossa causa")
        return reverse('apoio')

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
    

# View responsável por carregar o blog de notícias da categoria TDAH
class TDAHBlogView(ListView):
    template_name = 'blog/noticias_tdah.html'
    model = BlogPost
    context_object_name='noticias'    
    paginate_by = 9

    def get_queryset(self):
        try:
            categoria = Category.objects.get(name='TDAH')
            queryset = BlogPost.objects.filter(category=categoria).order_by('-date').select_related('category')
        except ObjectDoesNotExist:
            queryset = BlogPost.objects.none()

        return queryset

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            categoria = Category.objects.get(name='TDAH')            
        except ObjectDoesNotExist:
            categoria = 'TDAH'

        context['categoria'] = categoria           
        return context



# View responsável por carregar o blog de notícias da categoria TEA
class TEABlogView(ListView):
    template_name = 'blog/noticias_tea.html'
    model = BlogPost
    context_object_name='noticias'    
    paginate_by = 9

    def get_queryset(self):
        try:
            categoria = Category.objects.get(name='TEA')
            queryset = BlogPost.objects.filter(category=categoria).order_by('-date').select_related('category')
        except ObjectDoesNotExist:
            queryset = BlogPost.objects.none()

        return queryset
    
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            categoria = Category.objects.get(name='TEA')
        except ObjectDoesNotExist:
            categoria = 'TEA'

        context['categoria'] = categoria          
        return context


# View Responsável por carregar cada notícia    
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
    
class Blog(ListView):
    model = BlogPost
    template_name = 'blog/blog.html'
    context_object_name = 'post'
    ordering = '-date'
    paginate_by = 9 
  


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
        num_inscritos = Inscricao.objects.count()

        context['num_apoiadores'] = num_apoiadores
        context['num_carousel'] = num_carousel
        context['num_blogpost'] = num_blogpost
        context['num_category'] = num_category
        context['num_contatos'] = num_contatos
        context['num_depoimentos'] = num_depoimentos
        context['num_inscritos'] = num_inscritos
        return context


# Página de quem somos
class QuemSomos(TemplateView):
    template_name = 'quem-somos.html'

# Página Privacidade e Segurança
class Privacidade(TemplateView):
    template_name = 'privacidade.html'
