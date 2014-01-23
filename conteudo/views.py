from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django import forms
import datetime

class FormularioComentario(forms.Form):
    nome = forms.CharField(max_length = 100)
    email = forms.EmailField()
    comentario = forms.CharField(widget=forms.TextInput)


def sobre(request):
    '''Pagina sobre'''

    from conteudo.models import Pagina

    p = Pagina.objects.get(nome = 'sobre')

    return render_to_response('sobre.html',{
        'p': p,
        'cor': 'azul',
        'nome': 'sobre',
        })

def dados(request):
    '''Pagina sobre'''

    from conteudo.models import Pagina

    p = Pagina.objects.get(nome = 'dados')

    return render_to_response('sobre.html',{
        'p': p,
        'cor': 'azul',
        'nome': 'sobre',
        })




def post(request, slug=None):
    '''Pagina post'''
    
    from conteudo.models import Post
    from conteudo.models import Comentario

    if slug != None:
        post = Post.objects.get(slug = slug)
    else:
        post = Post.objects.filter(ativo = True).order_by('-data_publicacao')[0]

    lista_posts = Post.objects.filter(ativo = True).exclude(slug = post.slug).order_by('-data_publicacao')

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


    # Carrega comentarios

    comentarios = Comentario.objects.filter(post = post, moderado = False)


    return render_to_response('post.html', {
        'nome': 'blog',
        'cor': 'verde',
        'post': post,
        'lista_posts': lista_posts,
        'form': form,
        'comentarios': comentarios,
        })

