from django.contrib import admin
from import_export import resources

from .models import Usuario

# Register your models here.

class UsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario

class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ['username', 'first_name','last_name','email','foto','is_staff']
    list_display = ('username', 'first_name','last_name','email','foto','is_staff',)
    list_filter = ('first_name','last_name',)
    resource_class = UsuarioResource

admin.site.register(Usuario, UsuarioAdmin)