from django.urls import path
from .views import CarrouselView, CarouselCreateView, CarouselDetailView, CarouselUpdateView, CarouselDeleteView

urlpatterns = [
    path('carrousel/', CarrouselView.as_view(), name='carrousel_view'),
    path('carrousel/create/', CarouselCreateView.as_view(), name='carousel_create'),
    path('carrousel/<int:pk>/', CarouselDetailView.as_view(), name='carousel_detail'),
    path('carrousel/<int:pk>/update/', CarouselUpdateView.as_view(), name='carousel_update'),
    path('carrousel/<int:pk>/delete/', CarouselDeleteView.as_view(), name='carousel_delete'),
]