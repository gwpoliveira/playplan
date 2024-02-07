# administration/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import CarouselImage, Contato, BlogPost, BlogPostImage, Category, Apoiador
from .forms import CarouselImageForm, ContatoForm, BlogPostForm, BlogPostImageForm, ApoiadorForm, CategoryForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages

    # ************ Carrossel *************** #
class ImageListView(LoginRequiredMixin, ListView):
    model = CarouselImage
    template_name = 'administration/image_list.html'
    context_object_name = 'images'

class ImageCreateView(LoginRequiredMixin,CreateView):
    model = CarouselImage
    form_class = CarouselImageForm
    template_name = 'administration/add_image.html'
    success_url = reverse_lazy('image_list')

class ImageUpdateView(LoginRequiredMixin,UpdateView):
    model = CarouselImage
    form_class = CarouselImageForm
    template_name = 'administration/edit_image.html'
    success_url = reverse_lazy('image_list')

class ImageDeleteView(LoginRequiredMixin,DeleteView):
    model = CarouselImage
    template_name = 'administration/delete_image.html'
    success_url = reverse_lazy('image_list')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('image_list')
        else:
            return super().post(request, *args, **kwargs)
        
# ************ Contato *************** #
class ContatoCreateView(CreateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'contato/contato.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Mensagem enviada com sucesso!")
        return reverse('home')

class ContatoListView(LoginRequiredMixin,ListView):
    model = Contato
    template_name = 'contato/contato_list.html'
    context_object_name = 'contatos'

class ContatoDetailView(DetailView):
    model = Contato
    template_name = 'contato/contato_detail.html'
    context_object_name = 'contato'

# ************ Blogger *************** #
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_post_list.html'
    context_object_name = 'posts'
    paginate_by = 9 

class BlogPostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(BlogPost, pk=pk)
        images = BlogPostImage.objects.filter(post=post)
        return render(request, 'blog/blog_post_detail.html', {'post': post, 'images': images})

class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_post_form.html'
    success_url = reverse_lazy('blog_post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_post_form.html'
    success_url = reverse_lazy('blog_post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/blog_post_confirm_delete.html'
    success_url = reverse_lazy('blog_post_list')



# ************ Apoio *************** #
    
class ApoiadorCreateListView(CreateView, ListView):
    model = Apoiador
    form_class = ApoiadorForm
    template_name = 'apoio/apoio.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["apoiadores"] = Apoiador.objects.all()[:5]            
        return context

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Obrigado por apoiar nossa causa")
        return reverse('apoio')
    
class ListaApoiadores(LoginRequiredMixin, ListView):
    model = Apoiador
    template_name = 'apoio/lista.html'
    context_object_name='apoiadores'

    def get_queryset(self):
        search = self.request.GET.get("apoiador")
        
        if search:
            self.apoiadores = Apoiador.objects.filter(nome__icontains=search)
        else:
            self.apoiadores = Apoiador.objects.all()

        return self.apoiadores
    
class ApoiadorDetailView(LoginRequiredMixin, DetailView):
    model=Apoiador
    template_name='apoio/detalhar_apoiador.html'
    context_object_name='apoiador'
    pk_url_kwarg='id'
    
class ApoiadorDeleteView(LoginRequiredMixin, DeleteView):
    model=Apoiador
    template_name='apoio/apagar_apoiador.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Apoiador Apagado com sucesso!")
        return reverse('lista_de_apoiadores')
    

class ApoiadorUpdateView(LoginRequiredMixin, UpdateView):
    model=Apoiador
    template_name='apoio/atualizar_apoiador.html'
    form_class=ApoiadorForm
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Apoiador atualizado com sucesso!")
        return reverse('lista_de_apoiadores')
    

class ApoiadorCreateView(LoginRequiredMixin, CreateView):
    model=Apoiador
    template_name='apoio/novo_apoiador.html'
    form_class=ApoiadorForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Apoiador cadastrado com sucesso!")
        return reverse('lista_de_apoiadores')


# ************ Categorias de Postagem *************** #
    
class CriarCategoria(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'categorys/criar_categoria.html'
    form_class = CategoryForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Categoria criada com sucesso!")
        return reverse('listar-categorias')
    
class ListarCategorias(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'categorys/listar_categorias.html'
    context_object_name ='categorias'

class AtualizarCategoria(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'categorys/atualizar_categoria.html'
    form_class = CategoryForm
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Categoria atualizada com sucesso!")
        return reverse('listar-categorias')
    
class DetalharCategoria(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'categorys/detalhar_categoria.html'
    context_object_name = 'categoria'

class ApagarCategoria(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'categorys/apagar_categoria.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Categoria apagada com sucesso!")
        return reverse('listar-categorias')

