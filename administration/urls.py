# administration/urls.py
from django.urls import path
from .views import (
    ImageListView, ImageCreateView, ImageUpdateView, ImageDeleteView, 
    ContatoCreateView, ContatoListView, ContatoDetailView,
    BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView, ListaApoiadores, ApoiadorUpdateView, ApoiadorDetailView, ApoiadorCreateView
)

urlpatterns = [
    path('image_list/', ImageListView.as_view(), name='image_list'),
    path('add_image/', ImageCreateView.as_view(), name='add_image'),
    path('edit_image/<int:pk>/', ImageUpdateView.as_view(), name='edit_image'),
    path('delete_image/<int:pk>/', ImageDeleteView.as_view(), name='delete_image'),
    # path('contato/', ContatoCreateView.as_view(), name='contato'),
    path('contato_list/', ContatoListView.as_view(), name='contato_list'),
    path('contato_list/<int:pk>', ContatoDetailView.as_view(), name='contato_list'),
    
    #******************* Blog *******************#
    path('blog_post_list/', BlogPostListView.as_view(), name='blog_post_list'),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog_post_create/', BlogPostCreateView.as_view(), name='blog_post_create'),
    path('blog/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blog_post_edit'),
    path('blog/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blog_post_delete'),


    #******************* Administrativo *******************#
    path('lista_de_apoiadores/', ListaApoiadores.as_view(), name='lista_de_apoiadores'),
    path('apoiador/atualizar/<int:id>', ApoiadorUpdateView.as_view(), name='atualizar_apoiador'),
    path('apoiador/detalhar/<int:id>', ApoiadorDetailView.as_view(), name='detalhar_apoiador'),
    path('apoiador/novo/', ApoiadorCreateView.as_view(), name='criar_apoiador'),

    
    
]