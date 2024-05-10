from rest_framework import serializers
from .models import *


class CarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselImage
        fields = ['image', 'description', 'link', 'ativo', 'data']

class ContatoSerialiezer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'mensagem']

class BlogPostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostImage
        fields = ['post', 'image']

class ApoiadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apoiador
        fields = ['nome', 'email']

class DepoimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depoimento
        fields = ['imagem', 'nome', 'cargo', 'descricao', 'imagem_fundo', 'ativo', 'data']

class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = ['email']


class CategorySerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['name', 'about', 'link']

    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('detail-categoria-api', kwargs={'pk': obj.pk}))
        return None

class CriarPost(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'about', 'date', 'category', 'featured_image', 'description', 'destaque_home', 'img_description']

class BlogPostSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'about', 'date', 'category_name', 'featured_image', 'link']

    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('post-detalhe', kwargs={'slug': obj.slug}))
        return None
    

class DetalharPost(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None
    
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'about', 'date', 'category_name', 'featured_image', 'img_description', 'description']


