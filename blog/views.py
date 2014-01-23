# -*- coding: utf-8 -*-

from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django import forms
from django.core.paginator import Paginator
import datetime
from captcha.fields import CaptchaField


class FormularioComentario(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    comentario = forms.CharField(widget=forms.widgets.Textarea(attrs = {'placeholder':'Seu Comentário', 'rows':'2'}))
    captcha = CaptchaField()


def listagem(request, page=1):
    '''Tela inicial do blog'''

    from blog.models import Post
    from blog.models import Comentario
    from blog.models import Tag

    tags = Tag.objects.all()

    posts_por_pagina = 3
    page = int(page)

    posts = []

    if 'tag' in request.GET:
        filtro_tag = request.GET['tag']
        todos_posts = Post.objects.filter(tags__slug = filtro_tag).order_by('-data_publicacao')
    else:
        todos_posts = Post.objects.all().order_by('-data_publicacao')

    paginacao = Paginator(todos_posts, posts_por_pagina)
    pagina = paginacao.page(page)

    for p in pagina:
        comentarios = Comentario.objects.filter(post=p)
        posts.append({
            'titulo': p.titulo,
            'resumo': p.resumo,
            'data_publicacao': p.data_publicacao,
            'conteudo': p.conteudo,
            'comentarios': comentarios.count(),
            'slug': p.slug,
            'imagem_destaque': p.imagem_destaque,
        })

    # Pega os mais lidos
    mais_lidos = Post.objects.all().order_by('-data_publicacao')[:5]

    return render_to_response('blog/listagem.html', {
        'posts': posts,
        'page': page,
        'total_paginas': paginacao.num_pages,
        'has_next': pagina.has_next(),
        'has_previous': pagina.has_previous(),
        'next': page + 1,
        'previous': page - 1,
        'mais_lidos': mais_lidos,
        'tags': tags,
        'nome': 'blog',
    })


def post(request, slug):
    '''Pega o post'''

    from blog.models import Post
    from blog.models import Comentario

    post = Post.objects.get(slug=slug)
    post.contador_leitura += 1
    post.save()

    comentarios = Comentario.objects.filter(post=post)

    mais_lidos = Post.objects.all().order_by('-data_publicacao')[:5]

    if request.method == 'POST':
        form = FormularioComentario(request.POST)
        if form.is_valid():
            novo_comentario = Comentario()
            novo_comentario.post = post
            novo_comentario.data_hora = datetime.datetime.now()
            novo_comentario.nome = form.cleaned_data['nome']
            novo_comentario.email = form.cleaned_data['email']
            novo_comentario.comentario = form.cleaned_data['comentario']
            novo_comentario.ip = request.META['REMOTE_ADDR']
            novo_comentario.save()

    else:
        form = FormularioComentario()

    return render_to_response('blog/post.html', {
        'post': post,
        'comentarios': comentarios,
        'mais_lidos': mais_lidos,
        'form': form,
        'nome': 'blog',
    })
