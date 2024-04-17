# administration/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    #******************* Carrossel de Imagens *******************#
    path('image_list/', ImageListView.as_view(), name='image_list'),
    path('add_image/', ImageCreateView.as_view(), name='add_image'),
    path('edit_image/<int:pk>/', ImageUpdateView.as_view(), name='edit_image'),
    path('delete_image/<int:pk>/', ImageDeleteView.as_view(), name='delete_image'),
    path('detail-image/<int:pk>/', ImageDetail.as_view(), name='detail_image'),

    #******************* Contato *******************#
    # path('contato/', ContatoCreateView.as_view(), name='contato'),
    path('contato_list/', ContatoListView.as_view(), name='contato_list'),
    path('contato_list/<int:pk>', ContatoDetailView.as_view(), name='contato_list'),
    path('contato/atualizar/<int:id>', AtualizarContato.as_view(), name='atualizar_contato'),
    path('marcar_como_lida/<int:id>/', MarcarComoLida, name='marcar_como_lida' ),
    path('marcar_como_nao_lida/<int:id>/', MarcarComoNaoLida, name='marcar_como_nao_lida' ),

    
    #******************* Blog *******************#    
    path('lista_de_noticias/', ListaDeNotícias.as_view(), name='lista_de_noticias'),    
    path('blog_post_create/', BlogPostCreateView.as_view(), name='blog_post_create'),
    path('blog/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blog_post_edit'),
    path('blog/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blog_post_delete'),


    #******************* Administrativo *******************#
    path('lista_de_apoiadores/', ListaApoiadores.as_view(), name='lista_de_apoiadores'),
    path('apoiador/atualizar/<int:id>', ApoiadorUpdateView.as_view(), name='atualizar_apoiador'),
    path('apoiador/detalhar/<int:id>', ApoiadorDetailView.as_view(), name='detalhar_apoiador'),
    path('apoiador/apagar/<int:id>', ApoiadorDeleteView.as_view(), name='apagar_apoiador'),
    path('apoiador/novo/', ApoiadorCreateView.as_view(), name='criar_apoiador'),


    #******************* Categorias *******************#
    path('categorias/', ListarCategorias.as_view(), name='listar_categorias'),
    path('categorias/nova/', CriarCategoria.as_view(), name='criar_categoria'),
    path('categorias/detalhar/<int:id>', DetalharCategoria.as_view(), name='detalhar_categoria'),
    path('categorias/atualizar/<int:id>', AtualizarCategoria.as_view(), name='atualizar_categoria'),
    path('categorias/apagar/<int:id>', ApagarCategoria.as_view(), name='apagar_categoria'),
    
    #******************* Depoimento *******************#
    path('depoimento/', DepoimentoListView.as_view(), name='depoimento-list'),
    path('depoimento/<int:pk>/', DepoimentoDetailView.as_view(), name='depoimento-detail'),
    path('depoimento/novo/', DepoimentoCreateView.as_view(), name='depoimento-create'),
    path('depoimento/editar/<int:pk>/', DepoimentoUpdateView.as_view(), name='depoimento-update'),
    path('depoimento/deletar/<int:pk>/', DepoimentoDeleteView.as_view(), name='depoimento-delete'),
    
    #******************* New Letter *******************#
    path('inscricao/', inscricao_newsletter, name='inscricao_newsletter'),
    path('inscritos/', Inscritos.as_view(), name='inscritos'), 
    path('apagar_inscrito/<int:pk>/', ApagarInscrito.as_view(), name='apagar_inscrito'),
    path('detalhar_inscrito/<int:pk>/', DetalharInscrito.as_view(), name='detalhar_inscrito'),  
    path('atualizar_inscrito/<int:pk>/', AtualizarInscrito.as_view(), name='atualizar_inscrito'), 
    
]