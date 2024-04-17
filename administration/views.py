# administration/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import CarouselImage, Contato, BlogPost, BlogPostImage, Category, Apoiador, Depoimento, Inscricao
from .forms import InscricaoForm, AtualizaInscricao, CarouselImageForm, AtualizarApoiador, BlogPostForm, CategoryForm, UpdateContatoForm, DepoimentoForm, AtualizaCarouselImageForm, AtualizarDepoimentoForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib import messages
from django.db.models import Q

# ************ Carrossel *************** 
# View para listar as imagens do carrocel
class ImageListView(LoginRequiredMixin, ListView):
    model = CarouselImage
    template_name = 'administration/image_list.html'
    context_object_name = 'images'
    ordering='-data'
    paginate_by = 3

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        num_carousel = CarouselImage.objects.filter(ativo=True).count()
        context['num_carousel'] = num_carousel  
        return context

# View para criar/adicionar as imagens do carrocel
class ImageCreateView(LoginRequiredMixin,CreateView):
    model = CarouselImage
    form_class = CarouselImageForm
    template_name = 'administration/add_image.html'
    success_url = reverse_lazy('image_list')

# view para detalhar as imagens do carrocel
class ImageDetail(LoginRequiredMixin, DetailView):
    model = CarouselImage
    template_name = 'administration/image_detail.html'
    context_object_name = 'image'

# view para atualizar as imagens do carrocel
class ImageUpdateView(LoginRequiredMixin,UpdateView):
    model = CarouselImage
    form_class = AtualizaCarouselImageForm
    template_name = 'administration/edit_image.html'
    success_url = reverse_lazy('image_list')

# view para deletar imagens do carrocel.
class ImageDeleteView(LoginRequiredMixin,DeleteView):
    model = CarouselImage
    template_name = 'administration/delete_image.html'
    success_url = reverse_lazy('image_list')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('image_list')
        else:
            return super().post(request, *args, **kwargs)
        

# View para listar contatos
class ContatoListView(LoginRequiredMixin, ListView):
    model = Contato
    template_name = 'contato/contato_list.html'
    context_object_name = 'contatos'
    ordering = '-data'
    paginate_by = 10


    def get_queryset(self):            
        
        search = self.request.GET.get("pesquisa")
    
        if search:
            contatos = Contato.objects.filter(Q(nome__icontains=search) | Q(email__icontains=search))
        else:
            contatos = Contato.objects.all().order_by('-data')

        return contatos 



    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        num_contato = Contato.objects.count()
        context['num_contato'] = num_contato  
        return context

# View que mostra os detalhes do contato.
class ContatoDetailView(LoginRequiredMixin, DetailView):
    model = Contato
    template_name = 'contato/contato_detail.html'
    context_object_name = 'contato'

# View para atualizar os contatos.
class AtualizarContato(LoginRequiredMixin, UpdateView):
    model = Contato
    form_class = UpdateContatoForm
    template_name = 'contato/atualizar_contato.html'
    pk_url_kwarg='id'
    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Contato atualizado com sucesso!")
        return reverse('contato_list')
    
def MarcarComoLida(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    if not contato.lida:
        contato.lida = True
        contato.save()
        messages.success(request, 'Mensagem marcada como lida!')
        return redirect('contato_list')
    else:
        messages.info(request, 'Mensagem já está marcada como lida!')
        return redirect('contato_list')
    
def MarcarComoNaoLida(request, id):
    contato = get_object_or_404(Contato, id=id)
    if contato.lida:
        contato.lida = False
        contato.save()
        messages.success(request, 'Mensagem marcada como não lida!')
        return redirect('contato_list')
    else:
        messages.info(request, 'Mensagem já está marcada como não lida!')
        return redirect('contato_list')



# ************ Blogger *************** #
# View para criar postagens.
class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_post_form.html'
    success_url = reverse_lazy('lista_de_noticias')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# View para fazer alterações no blog.
class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_post_form.html'
    success_url = reverse_lazy('lista_de_noticias')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# View para deletar postagens do blog.
class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/blog_post_confirm_delete.html'
    success_url = reverse_lazy('lista_de_noticias')


# View responsável pela lista de notícias do Painel Administrativo
class ListaDeNotícias(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'administration/lista_de_noticias.html'
    context_object_name='posts'
    ordering='-date'
    paginate_by = 10

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        num_posts = BlogPost.objects.count()
        context['categories'] = Category.objects.all()
        context['num_posts'] = num_posts  
        return context

    # def get_queryset(self):            
    #     category = self.request.GET.get("category")
    #     search = self.request.GET.get("pesquisa")
    
    #     if search:
    #         noticias = BlogPost.objects.filter(Q(title__icontains=search) | Q(about__icontains=search))
    #     else:
    #         noticias = BlogPost.objects.all().order_by('-date')

    #     return noticias 
    
    def get_queryset(self):            
        category = self.request.GET.get("category")
        search = self.request.GET.get("pesquisa")

        if category:
            noticias = BlogPost.objects.filter(category__id=category).order_by('-date')
        elif search:
            noticias = BlogPost.objects.filter(Q(title__icontains=search) | Q(about__icontains=search))
        else:
            noticias = BlogPost.objects.all().order_by('-date')

        return noticias


# ************ Apoio *************** #  
# View que exibe uma lista de apoiadores.
class ListaApoiadores(LoginRequiredMixin, ListView):
    model = Apoiador
    template_name = 'apoio/lista.html'
    context_object_name='apoiadores'
    paginate_by = 10

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        num_apoiador = Apoiador.objects.count()
        context['num_apoiador'] = num_apoiador  
        return context

    def get_queryset(self):
        search = self.request.GET.get("pesquisa")
        
        if search:
            self.apoiadores = Apoiador.objects.filter(nome__icontains=search)
        else:
            self.apoiadores = Apoiador.objects.all()

        return self.apoiadores

# View que exibe informações detalhada sobre um único apoiador.
class ApoiadorDetailView(LoginRequiredMixin, DetailView):
    model=Apoiador
    template_name='apoio/detalhar_apoiador.html'
    context_object_name='apoiador'
    pk_url_kwarg='id'

# View mostra um usuário autenticado pode confirmar a deleção de um apoiador específico. 
class ApoiadorDeleteView(LoginRequiredMixin, DeleteView):
    model=Apoiador
    template_name='apoio/apagar_apoiador.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Apoiador Apagado com sucesso!")
        return reverse('lista_de_apoiadores')
    
# View para fornecer uma interface onde um usuário autenticado pode editar os detalhes de um apoiador específico.
class ApoiadorUpdateView(LoginRequiredMixin, UpdateView):
    model=Apoiador
    template_name='apoio/atualizar_apoiador.html'
    form_class=AtualizarApoiador
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Apoiador atualizado com sucesso!")
        return reverse('lista_de_apoiadores')
    
# View para fornecer uma interface onde um usuário autenticado pode adicionar um novo apoiador ao sistema.
class ApoiadorCreateView(LoginRequiredMixin, CreateView):
    model=Apoiador
    template_name='apoio/novo_apoiador.html'
    form_class=AtualizarApoiador
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Apoiador cadastrado com sucesso!")
        return reverse('lista_de_apoiadores')


# ************ Categorias de Postagem *************** #

#  View para fornecer uma interface onde um usuário autenticado pode adicionar uma nova categoria ao sistema.
class CriarCategoria(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'categorys/criar_categoria.html'
    form_class = CategoryForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Categoria criada com sucesso!")
        return reverse('listar_categorias')
    
# View que lista todas as categorias existentes no sistema.
class ListarCategorias(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'categorys/listar_categorias.html'
    context_object_name ='categorias'
    paginate_by = 2

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        num_categorias = Category.objects.count()
        context['num_categorias'] = num_categorias  
        return context


# View que um usuário autenticado atualiza as categorias existentes.
class AtualizarCategoria(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'categorys/atualizar_categoria.html'
    form_class = CategoryForm
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Categoria atualizada com sucesso!")
        return reverse('listar_categorias')
    
# View para para exibir detalhes específicos de uma categoria.
class DetalharCategoria(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'categorys/detalhar_categoria.html'
    context_object_name = 'categoria'
    pk_url_kwarg='id'

# View utilizada para fornecer uma interface onde um usuário autenticado pode confirmar a deleção de uma categoria específica.
class ApagarCategoria(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'categorys/apagar_categoria.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Categoria apagada com sucesso!")
        return reverse('listar_categorias')
    

# ************ Depoimento *************** # 
# View responsável para listar os depoimentos no painel administrativo
class DepoimentoListView(LoginRequiredMixin, ListView):
    model = Depoimento
    template_name = 'depoimento/depoimento_list.html'
    context_object_name = 'depoimentos'
    ordering='-data'
    paginate_by = 10

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        num_depoimentos = Depoimento.objects.count()
        context['num_depoimentos'] = num_depoimentos  
        return context

    def get_queryset(self):            
        
        search = self.request.GET.get("pesquisa")
    
        if search:
            depoimento = Depoimento.objects.filter(Q(nome__icontains=search) | Q(cargo__icontains=search))
        else:
            depoimento = Depoimento.objects.all()

        return depoimento 

# View responsável para detalhar os depoimentos no painel administrativo
class DepoimentoDetailView(LoginRequiredMixin, DetailView):
    model = Depoimento
    template_name = 'depoimento/depoimento_detail.html'
    context_object_name = 'depoimento'



# View responsável para criar os depoimentos no painel administrativo
class DepoimentoCreateView(LoginRequiredMixin, CreateView):
    model = Depoimento
    template_name = 'depoimento/depoimento_form.html'
    form_class = DepoimentoForm
    success_url = reverse_lazy('depoimento-list')
    

# View responsável para atualizar os depoimentos no painel administrativo
class DepoimentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Depoimento
    form_class = AtualizarDepoimentoForm
    success_url = reverse_lazy('depoimento-list')
    template_name = 'depoimento/depoimento_form.html'


# View responsável para apagar os depoimentos no painel administrativo
class DepoimentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Depoimento
    template_name = 'depoimento/depoimento_confirm_delete.html'
    success_url = reverse_lazy('depoimento-list')

# ************ News Letter *************** # 
def inscricao_newsletter(request):
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            inscricao = form.save()
            # Pode adicionar mais lógica aqui se necessário
            return render(request, 'confirmacao_inscricao.html', {'email': inscricao.email})
    else:
        form = InscricaoForm()

    return render(request, 'inscricao_newsletter.html', {'form': form})
    
# view para listar inscritos
class Inscritos(LoginRequiredMixin, ListView):
    model = Inscricao
    template_name = 'administration/assinantes.html'
    context_object_name = 'assinantes'
    paginate_by = 10

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        num_inscritos = Inscricao.objects.count()
        context['num_inscritos'] = num_inscritos  
        return context
    
    def get_queryset(self):            
        
        search = self.request.GET.get("pesquisa")
    
        if search:
            inscritos = Inscricao.objects.filter(email__icontains=search)
        else:
            inscritos = Inscricao.objects.all()

        return inscritos 
    


# view para detalhar inscrito
class DetalharInscrito(LoginRequiredMixin, DetailView):
    model = Inscricao
    template_name = 'administration/detalhar_inscrito.html'
    context_object_name = 'inscrito'

# view para atualizar inscrito
class AtualizarInscrito(LoginRequiredMixin,UpdateView):
    model = Inscricao
    form_class = AtualizaInscricao
    template_name = 'administration/edita_inscrito.html'
    success_url = reverse_lazy('inscritos')

# view para deletar inscrito
class ApagarInscrito(LoginRequiredMixin,DeleteView):
    model = Inscricao
    template_name = 'administration/apagar_inscrito.html'    

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Inscrito Apagado com sucesso!")
        return reverse('inscritos')