from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    '''Pagina inicial - Estatica por enquanto'''

    from blog.models import Post

    posts = Post.objects.filter(ativo = True, destaque = False).order_by('-data_publicacao')[:3]
    destaques = Post.objects.filter(ativo = True, destaque = True).order_by('-data_publicacao')[:3]
    count = range(0, len(destaques))

    return render_to_response('index.html',{
        'posts': posts,
        'destaques': destaques,
        'count': count,
        })

def mapa(request):
    ''' Pagina do mapa - Estatica '''
    # TODO: Torna-la dinamica
    # TODO: Recortar as secoes de templates

    return render_to_response('mapa.html', {
        'nome': 'mapa',
        'cor': 'laranja',
        })


def dados(request):
    ''' Pagina do Dados - Estatica '''
    # TODO: Torna-la dinamica

    return render_to_response('dados.html', {
        'nome': 'dados',
        'cor': 'limao',
        })

def cadastro(request):
    ''' Pagina do Cadastro - Estatica '''
    # TODO: Torna-la dinamica

    return render_to_response('cadastro.html', {})

def carousel(request):
    ''' Pagina do Cadastro - Estatica '''
    # TODO: Torna-la dinamica

    return render_to_response('carousel.html', {})

def busca(request):
    '''Combo de busca UF/Municipio'''

    from ibge.models import Uf
    from ibge.models import Municipio

    if request.method == 'POST':
        if 'uf' in request.POST and 'cidade' in request.POST:
            uf = request.POST['uf']
            slug = request.POST['cidade']
            return HttpResponseRedirect('/mapa/' + uf + "/" + slug + "/" )

    ufs = Uf.objects.all().order_by('sigla')

    return render_to_response('busca.html', {
        'ufs': ufs,
        })

def busca_mun(request):
    '''Recebe o post uf e retorna as cidades'''

    if request.method == 'POST':
        uf = request.POST['uf']

        from ibge.models import Municipio
        mun = Municipio.objects.filter(estado__sigla = uf).order_by('nome')

        return render_to_response('busca_mun.html', {
            'mun': mun
            })

    return HttpResponse('err')


def busca_escola(request):
    '''Faz a busca por nome ou parte do nome da escola'''

    if request.method == 'POST':
        escola = request.POST['escola']

        from escola.models import Escola 
        escolas = Escola.objects.filter(nome__icontains = escola, latlong__isnull = False)

    return render_to_response('busca_escola.html', {
        'escolas': escolas,
        'quantidade': escolas.count()
        })
