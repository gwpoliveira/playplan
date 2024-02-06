from django.db import models


class CarouselImage(models.Model):
    image = models.ImageField('Imagem',upload_to='carousel_images/')
    description = models.CharField('Descrição',max_length=255)

    def __str__(self):
        return self.description
    
class Contato(models.Model):
    STATUS = (
        (True, 'Respondida'),
        (False,'Não Respondida'),
    )
    nome = models.CharField('nome', blank=False, null=False, max_length=155)
    email = models.EmailField('e-mail', blank=False, null=False,max_length=255)
    telefone = models.CharField('telefone', blank=False,null=False,max_length=20)
    mensagem = models.TextField('mensagem', blank=True, null=True, max_length=500)
    status = models.BooleanField(
        max_length=30,
        choices=STATUS,
        default=False,
    )

    def __str__(self):
        return f"{self.nome}"
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='blog_featured_images/')
    text = models.TextField()

    def __str__(self):
        return self.title

class BlogPostImage(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')