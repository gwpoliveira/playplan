from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CarouselImage

class CarrouselView(TemplateView):
    template_name = 'administration/carrousel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel_images'] = CarouselImage.objects.all()
        return context

class CarouselCreateView(CreateView):
    model = CarouselImage
    template_name = 'administration/carouselimage_form.html'
    fields = ['image', 'description']
    success_url = reverse_lazy('carrousel_view')

class CarouselDetailView(DetailView):
    model = CarouselImage
    template_name = 'administration/carouselimage_detail.html'

class CarouselUpdateView(UpdateView):
    model = CarouselImage
    template_name = 'administration/carouselimage_form.html'
    fields = ['image', 'description']
    success_url = reverse_lazy('carrousel_view')

class CarouselDeleteView(DeleteView):
    model = CarouselImage
    template_name = 'administration/carouselimage_confirm_delete.html'
    success_url = reverse_lazy('carrousel_view')