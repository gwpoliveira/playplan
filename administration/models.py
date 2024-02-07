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
    nome = models.CharField('nome', max_length=155)
    email = models.EmailField('e-mail', max_length=255)
    telefone = models.CharField('telefone', blank=False,null=False,max_length=20)
    mensagem = models.TextField('mensagem', max_length=500)
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
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

# ************** blog **************#
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField("descrição")
    date = models.DateField("data da publicação",)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='blog_featured_images/')
    text = models.TextField()

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