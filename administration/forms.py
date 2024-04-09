from ckeditor.fields import RichTextField
from django import forms
from .models import Inscricao, CarouselImage, Contato, BlogPost, BlogPostImage, Apoiador, Category, Depoimento
from django.utils.text import slugify

# ************ Banner do Carrossel ****************

class CarouselImageForm(forms.ModelForm):
    class Meta:
        model = CarouselImage
        fields = ['image','description', 'link']


class AtualizaCarouselImageForm(forms.ModelForm):
    class Meta:
        model = CarouselImage
        fields = ['image','description', 'link', 'ativo']

# ************ Formulário do Contato ****************

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome','email','telefone','mensagem',]

class UpdateContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['lida', 'status']


# ************ Formulário do Blog ****************

class BlogPostForm(forms.ModelForm):
    
    class Meta:
        model = BlogPost
        fields = ('title', 'about', 'date', 'category', 'featured_image', 'img_description' , 'description', 'destaque_home')

class BlogPostImageForm(forms.ModelForm):
    class Meta:
        model = BlogPostImage
        fields = ['image']


class BlogPostFormAdmin(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__' 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'slug' not in self.fields:  
            self.fields['slug'] = forms.SlugField(max_length=255, required=False)  

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.slug: 
            instance.slug = "{}/{}/{}/{}/{}".format(
                instance.category.name,
                instance.date.strftime('%d'),
                instance.date.strftime('%m'),
                instance.date.strftime('%Y'),
                slugify(instance.title))
        if commit and instance is not None:
            instance.save()
        return instance

# ************ Formulário do Apoaidor **************** #
class ApoiadorForm(forms.ModelForm):
    class Meta:
        model = Apoiador
        fields=['nome', 'email']

class AtualizarApoiador(forms.ModelForm):
    class Meta:
        model = Apoiador
        fields='__all__'

# ************ Formulário do Categoria **************** #
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields='__all__'        
        
# ************ Formulário do Depoimento **************** #
class DepoimentoForm(forms.ModelForm):
    class Meta:
        model = Depoimento
        fields = ['imagem', 'nome', 'cargo', 'descricao', 'imagem_fundo']


class AtualizarDepoimentoForm(forms.ModelForm):
    class Meta:
        model = Depoimento
        fields = ['imagem', 'nome', 'cargo', 'descricao', 'imagem_fundo', 'ativo']

# ************ New Letter **************** #
class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['email']

    def save(self, commit=True):
        inscricao = super().save(commit=False)
        inscricao.confirmado = False  # Defina como True se desejar confirmar automaticamente
        if commit:
            inscricao.save()
        return inscricao
    
# ************ Atualização de Assinante **************** #
    
class AtualizaInscricao(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['email', 'confirmado']