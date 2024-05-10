from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'about']

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


