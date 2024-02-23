from ckeditor.fields import RichTextField
from django import forms
from .models import Inscricao, CarouselImage, Contato, BlogPost, BlogPostImage, Apoiador, Category, Depoimento

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
    # description = RichTextField()
    class Meta:
        model = BlogPost
        fields = ('title', 'about', 'date', 'category', 'featured_image', 'description', 'destaque_home', 'slug')

class BlogPostImageForm(forms.ModelForm):
    class Meta:
        model = BlogPostImage
        fields = ['image']

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