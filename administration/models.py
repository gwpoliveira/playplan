from django.db import models


class CarouselImage(models.Model):
    image = models.ImageField('Imagem',upload_to='carousel_images/')
    description = models.CharField('Descrição',max_length=255)

    def __str__(self):
        return self.description