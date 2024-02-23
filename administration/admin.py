from django.contrib import admin
from .models import Inscricao, CarouselImage,Contato, BlogPost, BlogPostImage, Category, Apoiador,Depoimento

admin.site.register(CarouselImage)
admin.site.register(Contato)

admin.site.register(BlogPostImage)
admin.site.register(Category)
admin.site.register(Apoiador)
admin.site.register(Depoimento)
admin.site.register(Inscricao)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    prepopulated_fields = {"slug": ("category", "title")}


admin.site.register(BlogPost, BlogPostAdmin)