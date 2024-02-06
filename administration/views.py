# administration/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import CarouselImage, Contato
from .forms import CarouselImageForm, ContatoForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages

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

