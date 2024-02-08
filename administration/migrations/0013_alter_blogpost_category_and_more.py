from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0012_alter_contato_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='featured_image',
            field=models.ImageField(upload_to='blog_featured_images/', verbose_name='Imagem de Destaque'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
    ]
