from django import forms
from .models import CarouselImage, Contato
class CarouselImageForm(forms.ModelForm):
    class Meta:
        model = CarouselImage
        fields = ['image','description']

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome','email','telefone','mensagem']