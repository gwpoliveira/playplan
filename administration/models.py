from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify

class CarouselImage(models.Model):
    image = models.ImageField('Imagem',upload_to='carousel_images/')
    description = models.CharField('Descrição', max_length=255)
    link = models.URLField(blank=True, null=True)
    ativo = models.BooleanField(default=True)
    data = models.DateTimeField(default=timezone.now)


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
    about = models.TextField("Descrição", max_length=200, blank=True, null=True)

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
    description=CKEditor5Field('Post: ', config_name='extends', blank=True, null=True)
    destaque_home = models.BooleanField(default=True)
    slug = models.SlugField(default="", max_length=255, editable=False ,unique=True, blank = True)
    img_description = models.CharField('Descrição da Imagem', blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = slugify(self.title) 
    #     else:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        elif self.title != BlogPost.objects.get(id=self.id):
            pass

        super().save(*args, **kwargs)


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
    visivel = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Apoiador"
        verbose_name_plural = "Apoiadores"
        

# ************** depoimento **************#
class Depoimento(models.Model):
    imagem = models.ImageField(upload_to='depoimentos/')
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descricao = CKEditor5Field('Depoimento: ', blank=True, null=True)
    imagem_fundo = models.ImageField(upload_to='depoimentos/backgrounds/', null=True, blank=True)
    ativo = models.BooleanField(default=True)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome
    
# ************** New Letter **************#
class Inscricao(models.Model):
    email = models.EmailField(unique=True)
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return self.email

@receiver(post_save, sender=Inscricao)
def enviar_email_confirmacao(sender, instance, created, **kwargs):
    if created:
        assunto = 'Confirmação de Inscrição'
        mensagem = f'Obrigado por se inscrever! Seu e-mail ({instance.email}) foi cadastrado com sucesso.'
        remetente = 'playplan@faespi.com.br'
        destinatario = [instance.email]

        send_mail(assunto, mensagem, remetente, destinatario)