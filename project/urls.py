from django.contrib import admin
from django.urls import include, path
from .views import HomeView, UserProfileView
from .views import HomeView,ContatoView, BlogView, NoticiaView, OQueETDAH, ApoioView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('', HomeView.as_view(), name='home'),
    path('contato/',ContatoView.as_view(), name='contato'),
    path('noticias/', BlogView.as_view(), name='noticias'),
    path('postagem/', NoticiaView.as_view(), name='postagem'),
    path('noticia1/', OQueETDAH.as_view(), name='o_que_e_tdah'),
    path('apoio/', ApoioView.as_view(), name='apoio'),
    path('administration/', include('administration.urls')), 
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

