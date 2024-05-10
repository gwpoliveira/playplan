from django.contrib import admin
from django.urls import include, path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from administration.views import *

# 
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('quemsomos/', QuemSomos.as_view(), name='quem-somos'),
    path('privacidade/', Privacidade.as_view(), name='privacidade'),
    path('noticias_tdah/', TDAHBlogView.as_view(), name='noticias-tdah'),
    path('noticias_tea/', TEABlogView.as_view(), name='noticias-tea'),
    path('blog/', Blog.as_view(), name='blog'),
    path('postagem/<path:slug>', postagem, name='postagem'),    
    path('apoio/', apoio, name='apoio'),
    path('administration/', include('administration.urls')), 
    path('admin/', admin.site.urls),
    path('paineladm/', painel, name='painel_adm'),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    ############## API / Django Rest FrameWork ##################
    path('api/links/', getRoutes, name='get-routes'), 
    path("api/posts/", Posts.as_view({'get': 'list'}), name='posts-api'),
    path("api/posts/categorias/", Categorias.as_view({'get': 'list'}), name='posts-categorias'),
    path("api/posts/tea/", PostsTEA.as_view({'get': 'list'}), name='posts-tea'),
    path("api/posts/tdah/", PostsTDAH.as_view({'get': 'list'}), name='posts-tdah'),
    path('api/posts/detalhar/<path:slug>/', DetalharPost.as_view(), name='post-detalhe'),
    path('api/posts/nova-postagem/', CriarPost.as_view(), name='novo-post-api'),
    path('api/posts/categorias/nova/', CriarCategoria.as_view(), name='nova-categoria-api'),
    path('api/posts/categorias/detail/<int:pk>/', CategoriaDetail.as_view(), name='detail-categoria-api'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



