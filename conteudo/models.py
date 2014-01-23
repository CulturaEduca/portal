# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib import admin
import datetime

# class Categoria(models.Model):
#     '''Separador de conteudo'''

#     titulo = models.CharField('Nome da Categoria', max_length=30)

#     def __unicode__(self):
#         return self.titulo


# class Tags(models.Model):
#     '''Tags para postagens'''

#     nome = models.CharField('Tag', max_length=50)

#     def __unicode__(self):
#         return self.nome

#     class Meta:
#         verbose_name = 'Tag'
#         verbose_name_plural = 'Tags'

# class Post(models.Model):
#     '''Posts e artigos'''

#     categoria = models.ForeignKey(Categoria)
#     titulo = models.CharField(u'Título', max_length=100)
#     conteudo = models.TextField(u'Conteúdo')
#     resumo = models.CharField(u'Resumo do conteúdo', null=True, blank=True, help_text='Se o resumo estiver em branco, os 160 caracteres iniciais do post será exibido', max_length=200)
#     tags = models.ManyToManyField(Tags)
#     imagem_destaque = models.ImageField(upload_to='destaque', help_text='Imagem de Destaque, se não tiver, aparece padrão', null=True, blank=True)
#     ativo = models.BooleanField('Post Ativo', help_text = 'Marque para deixar ativo, desmarcado = rascunho')
#     destaque = models.BooleanField('Destaque', help_text = 'Marque para deixar em destaque')
#     data_publicacao = models.DateTimeField(u'Data da publicação', default=datetime.datetime.now())
#     slug = models.SlugField('URL', null=True, blank=True, editable=False, unique=True, max_length=255)

#     def save(self):
#         self.slug = slugify(self.titulo)
#         super(Post, self).save()

#     def get_absolute_url(self):
#         return '/blog/%s/' % self.slug

#     def __unicode__(self):
#         return self.titulo

#     class Meta:
#         verbose_name = 'Post (blog)'
#         verbose_name_plural = 'Posts (blog)'

class Pagina(models.Model):
    '''Paginas estaticas'''

    nome = models.CharField(u'URL', max_length=40)
    titulo = models.CharField(u'Título da página', max_length=100)
    conteudo = models.TextField(u'Conteúdo')

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Página Estática'
        verbose_name_plural = 'Páginas Estáticas'

# class Comentario(models.Model):
#     '''Comentario de usuarios'''

#     post = models.ForeignKey(Post)
#     titulo = models.CharField('Titulo do comentario', max_length=255, null=True, blank=True)
#     comentario = models.TextField('Comentario')
#     nome = models.CharField('Nome Usuario', max_length=200)
#     email = models.EmailField('Email do Usuario')
#     ip = models.IPAddressField('Ip do Usuario')
#     moderado = models.BooleanField('Moderar comentario')
#     data_hora = models.DateTimeField('Data/Hora', default=datetime.datetime.now())

#     def __unicode__(self):
#         return self.nome

#     class Meta:
#         verbose_name = 'Comentário'
#         verbose_name_plural = 'Comentários'

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('titulo','categoria','data_publicacao','slug','destaque','ativo',)
#     search_fields = ('titulo','conteudo',)
#     list_filter = ('categoria','ativo','destaque',)

#     class Media:
#         js = [
#             '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
#             '/static/js/tinymce_setup.js',
#             ]

# class ComentarioAdmin(admin.ModelAdmin):
#     list_display = ('post','nome','email','ip','data_hora','comentario','moderado',)
#     search_fields = ('nome',)
#     list_filter = ('moderado',)

class PaginaAdmin(admin.ModelAdmin):
    list_display = ('nome','titulo',)
    class Media:
        js = [
        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/js/tinymce_setup.js',
        ]

#admin.site.register(Post, PostAdmin)
admin.site.register(Pagina, PaginaAdmin)
#admin.site.register(Categoria)
#admin.site.register(Tags)
#admin.site.register(Comentario, ComentarioAdmin)