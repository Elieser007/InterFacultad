from django.db import models
from Apps.Usuario.models import Usuario
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la categoria',
                              max_length=50, blank=False, null=False)
    estado = models.BooleanField(
        'Categoria activada/Categoria no activada', default=True)
    fecha_creacion = models.DateTimeField(
        'Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre



class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField("Titulo", max_length=100, blank=False, null=False)
    slug = models.CharField("Slug", max_length=100, blank=False, null=False)
    descripcion=models.CharField("Descripción", max_length=200,blank=False, null=False)
    miniatura= models.URLField("Imagen Miniatura", max_length=200,blank=False,null=False)
    imagen= models.URLField("Imagen Principal", max_length=200,blank=False,null=False)
    autor=models.ForeignKey(Usuario, verbose_name="Autor", on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria, verbose_name="Categoria", on_delete=models.CASCADE)
    contenido= RichTextField()
    fecha_creacion = models.DateTimeField(
        "Fecha de Creacion", auto_now=False, auto_now_add=True)
    estado= models.BooleanField("Publicado/No Publicado",default=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['fecha_creacion']

    def __str__(self):
        return self.titulo

