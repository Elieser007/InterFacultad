from django.contrib import admin
from import_export import resources

from .models import Categoria, Post
# Register your models here.


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria



class PostResource(resources.ModelResource):
    class Meta:
        model = Post


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'fecha_creacion')
    resource_class = CategoriaResource


class PostAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'descripcion','categoria']
    list_display = ('titulo', 'slug','descripcion', 'categoria',)
    list_filter = ('fecha_creacion',)
    resource_class = PostResource


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post,PostAdmin)
