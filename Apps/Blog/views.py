from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Post,Categoria



# Create your views here.

# renderiza el inicio de la pagina
def home(request):
    search=request.GET.get('buscar')
    posts = Post.objects.filter(estado=True)
    if search:
        posts=Post.objects.filter(estado=True and
            Q(titulo__icontains=search) |
            Q(descripcion__icontains=search)
        ).distinct()

    paginator= Paginator(posts,2)   #instancia de paginator
    page=request.GET.get('page')    #obtenenmos la pagina actual en la que nos encontramos
    posts= paginator.get_page(page) # le pedimos a la instancia paginator la pagina en la que estamos

    return render(request, 'Pagina/blog.html', {'posts':posts})

# renderiza los detalles completos del post seleccionado
def detallePost(request,slug):
        post = get_object_or_404(Post,slug = slug )
        return render(request, 'Pagina/post.html', {'detallePost':post})

# renderiza la seccion de generales
def generales(request):
    posts=""
    search=request.GET.get('buscar')
    posts = Post.objects.filter(estado=True,
        categoria=Categoria.objects.get(nombre__iexact = 'Generales')
    )
    if search:
        posts=Post.objects.filter(
            Q(titulo__icontains=search) |
            Q(descripcion__icontains=search),
            estado=True, 
            categoria = 'Generales'
        ).distinct()

    paginator= Paginator(posts,2)   #instancia de paginator
    page=request.GET.get('page')    #obtenenmos la pagina actual en la que nos encontramos
    posts= paginator.get_page(page) # le pedimos a la instancia paginator la pagina en la que estamos

    return render(request, 'generales.html',{'posts':posts})

# renderiza la seccion de programacion
def programacion(request):
    posts=""
    search=request.GET.get('buscar')
    posts = Post.objects.filter(estado=True,
        categoria=Categoria.objects.get(nombre__iexact = 'Programacion')
    )
    if search:
        posts=Post.objects.filter(
            Q(titulo__icontains=search) |
            Q(descripcion__icontains=search),
            estado=True, 
            categoria=Categoria.objects.get(nombre__iexact = 'Programacion')
        ).distinct()

    paginator= Paginator(posts,2)   #instancia de paginator
    page=request.GET.get('page')    #obtenenmos la pagina actual en la que nos encontramos
    posts= paginator.get_page(page) # le pedimos a la instancia paginator la pagina en la que estamos

    return render(request, 'programacion.html',{'posts':posts})

# renderiza la seccion de videojuegos
def videojuegos(request):
    posts=""
    search=request.GET.get('buscar')
    posts = Post.objects.filter(estado=True,
        categoria=Categoria.objects.get(nombre__iexact = 'Videojuegos')
    )
    if search:
        posts=Post.objects.filter(
            Q(titulo__icontains=search) |
            Q(descripcion__icontains=search),
            estado=True, 
            categoria=Categoria.objects.get(nombre__iexact = 'Videojuegos')
        ).distinct()

    paginator= Paginator(posts,2)   #instancia de paginator
    page=request.GET.get('page')    #obtenenmos la pagina actual en la que nos encontramos
    posts= paginator.get_page(page) # le pedimos a la instancia paginator la pagina en la que estamos

    return render(request, 'videojuegos.html',{'posts':posts})

# renderiza la seccion de tecnologia
def tecnologia(request):
    posts=""
    search=request.GET.get('buscar')
    posts = Post.objects.filter(estado=True,
        categoria=Categoria.objects.get(nombre__iexact = 'Tecnologia')
    )
    if search:
        posts=Post.objects.filter(
            Q(titulo__icontains=search) |
            Q(descripcion__icontains=search),
            estado=True, 
            categoria=Categoria.objects.get(nombre__iexact = 'Tecnologia')
        ).distinct()

    paginator= Paginator(posts,2)   #instancia de paginator
    page=request.GET.get('page')    #obtenenmos la pagina actual en la que nos encontramos
    posts= paginator.get_page(page) # le pedimos a la instancia paginator la pagina en la que estamos

    return render(request, 'tecnologia.html',{'posts':posts})

# renderiza la seccion de tutoriales
def tutoriales(request):
    posts=""
    search=request.GET.get('buscar')
    posts = Post.objects.filter(estado=True,
        categoria=Categoria.objects.get(nombre__iexact = 'Tutoriales')
    )
    if search:
        posts=Post.objects.filter(
            Q(titulo__icontains=search) |
            Q(descripcion__icontains=search),
            estado=True, 
            categoria=Categoria.objects.get(nombre__iexact = 'Tutoriales')
        ).distinct()

    paginator= Paginator(posts,2)   #instancia de paginator
    page=request.GET.get('page')    #obtenenmos la pagina actual en la que nos encontramos
    posts= paginator.get_page(page) # le pedimos a la instancia paginator la pagina en la que estamos

    return render(request, 'tutoriales.html',{'posts':posts})