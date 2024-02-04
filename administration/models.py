from django.db import models


class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description