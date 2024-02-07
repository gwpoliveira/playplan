from ckeditor.fields import RichTextField
from django import forms
from .models import CarouselImage, Contato, BlogPost, BlogPostImage, Apoiador

class CarouselImageForm(forms.ModelForm):
    class Meta:
        model = CarouselImage
        fields = ['image','description']

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome','email','telefone','mensagem']

class BlogPostForm(forms.ModelForm):
    text = RichTextField()
    class Meta:
        model = BlogPost
        fields = ['title', 'about', 'date', 'category', 'featured_image', 'text']

class BlogPostImageForm(forms.ModelForm):
    class Meta:
        model = BlogPostImage
        fields = ['image']


class ApoiadorForm(forms.ModelForm):
    class Meta:
        model = Apoiador
        fields='__all__'