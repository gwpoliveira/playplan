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


class ContatoListSerialiezer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'data', 'lida', 'status', 'link']

    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('detail-contato-api', kwargs={'pk': obj.pk}))
        return None

class ContatoDetailSerialiezer(serializers.ModelSerializer):
    marcar_como_lida = serializers.SerializerMethodField()
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'data', 'mensagem', 'lida', 'status', 'marcar_como_lida']

    def get_marcar_como_lida(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('marcar-como-lida-api', kwargs={'pk': obj.pk}))
        return None


class BlogPostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostImage
        fields = ['post', 'image']

class ApoiadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apoiador
        fields = ['nome', 'email']

class ApoiadorSerializerADM(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    class Meta:
        model = Apoiador
        fields = ['nome', 'email', 'visivel', 'link']

    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('detail-apoio-api', kwargs={'pk': obj.pk}))
        return None

class DepoimentoSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    class Meta:
        model = Depoimento
        fields = ['imagem', 'nome', 'cargo', 'descricao', 'imagem_fundo', 'ativo', 'data', 'link']

    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('detail-depoimento-api', kwargs={'pk': obj.pk}))
        return None

class InscricaoSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    class Meta:
        model = Inscricao
        fields = ['id','email', 'link']

    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('detail-inscricao-api', kwargs={'pk': obj.pk}))
        return None

class InscricaoSerializerUser(serializers.ModelSerializer):
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
    category = serializers.ReadOnlyField(source='category.name')
    link = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'about', 'date', 'category', 'featured_image', 'link']

    def get_link(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('post-detalhe', kwargs={'slug': obj.slug}))
        return None
    

class DetalharPost(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')
    
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'about', 'date', 'category', 'featured_image', 'img_description', 'description']


