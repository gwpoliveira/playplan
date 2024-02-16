from django.contrib import admin
from django.urls import include, path
from .views import HomeView, UserProfileView, ApoiadorCreateListView, ContatoCreateView
from .views import HomeView, TDAHBlogView, TEABlogView, NoticiaView, QuemSomos, PainelAdm
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

# 
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('', HomeView.as_view(), name='home'),
    path('contato/', ContatoCreateView.as_view(), name='contato'),
    path('quemsomos/', QuemSomos.as_view(), name='quem-somos'),
    path('noticias_tdah/', TDAHBlogView.as_view(), name='noticias-tdah'),
    path('noticias_tea/', TEABlogView.as_view(), name='noticias-tea'),
    path('postagem/<int:id>', NoticiaView.as_view(), name='postagem'),    
    path('apoio/', ApoiadorCreateListView.as_view(), name='apoio'),
    path('administration/', include('administration.urls')), 
    path('admin/', admin.site.urls),
    path('paineladm/', PainelAdm.as_view(), name='painel_adm'),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



