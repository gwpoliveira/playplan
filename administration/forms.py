from ckeditor.fields import RichTextField
from django import forms
from .models import CarouselImage, Contato, BlogPost, BlogPostImage, Apoiador, Category

# ************ Banner do Carrossel ****************

class CarouselImageForm(forms.ModelForm):
    class Meta:
        model = CarouselImage
        fields = ['image','description', 'link']


# ************ Formulário do Contato ****************

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome','email','telefone','mensagem']

class UpdateContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'


# ************ Formulário do Blog ****************

class BlogPostForm(forms.ModelForm):
    # description = RichTextField()
    class Meta:
        model = BlogPost
        fields = ('title', 'about', 'date', 'category', 'featured_image', 'description')

class BlogPostImageForm(forms.ModelForm):
    class Meta:
        model = BlogPostImage
        fields = ['image']


class ApoiadorForm(forms.ModelForm):
    class Meta:
        model = Apoiador
        fields='__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields='__all__'