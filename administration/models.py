from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

class CarouselImage(models.Model):
    image = models.ImageField('Imagem',upload_to='carousel_images/')
    description = models.CharField('Descrição', max_length=255)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
    
class Contato(models.Model):
    STATUS = (
        (True, 'Respondida'),
        (False,'Não Respondida'),
    )
    nome = models.CharField('nome', max_length=155)
    email = models.EmailField('e-mail', max_length=255)
    telefone = models.CharField('telefone', blank=False,null=False,max_length=20)
    data = models.DateTimeField(default=timezone.now)
    mensagem = models.TextField('mensagem', max_length=500)
    lida = models.BooleanField(default=False)
    status = models.BooleanField(
        max_length=30,
        choices=STATUS,
        default=False,
    )    

    def __str__(self):
        return f"{self.nome}"
    

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
    
# ************** categorias de postagem **************#

class Category(models.Model):
    name = models.CharField("Nome", max_length=100)
    about = models.TextField("Descrição", max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

# ************** blog **************#
class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título")
    about = models.TextField("Resumo", max_length=200)
    date = models.DateField("Data da publicação",)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoria")
    featured_image = models.ImageField(upload_to='blog_featured_images/', verbose_name="Imagem de Destaque")
    text=CKEditor5Field('Post: ', config_name='extends')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

class BlogPostImage(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')


# ************** apoiador **************#

class Apoiador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Apoiador"
        verbose_name_plural = "Apoiadores"