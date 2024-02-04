from django import forms
from .models import CarrosselImagem

class CarrosselImagemForm(forms.ModelForm):
    class Meta:
        model = CarrosselImagem
        fields = ['imagem']