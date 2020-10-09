from import_export import resources
from django.contrib import admin

from .models import *

# Register your models here.
class UniversidadResource(resources.ModelResource):
    class Meta:
        model = Universidad

class FacultadResource(resources.ModelResource):
    class Meta:
        model = Facultad
class CarreraResource(resources.ModelResource):
    class Meta:
        model = Carrera
class AlumnoResource(resources.ModelResource):
    class Meta:
        model = Alumno
class DeporteMasculinoResource(resources.ModelResource):
    class Meta:
        model = DeporteMasculino
        
class DeporteFemeninoResource(resources.ModelResource):
    class Meta:
        model = DeporteFemenino

class DeporteResource(resources.ModelResource):
    class Meta:
        model = Deporte



class UniversidadAdmin(admin.ModelAdmin):
    search_fields = ['nombre','nombre_corto']
    list_display = ('id','nombre', 'nombre_corto',)
    resource_class = UniversidadResource

class FacultadAdmin(admin.ModelAdmin):
    search_fields = ['universidad','nombre','nombre_corto','especialidad']
    list_display = ('id','universidad','nombre', 'nombre_corto','especialidad',)
    resource_class = FacultadResource

class CarreraAdmin(admin.ModelAdmin):
    search_fields = ['nombre','nombre_corto','facultad','año']
    list_display = ('id','nombre', 'nombre_corto','facultad','año',)
    resource_class = CarreraResource

class AlumnoAdmin(admin.ModelAdmin):
    search_fields = ['nombres','apellidos','sexo','descripcion','carrera']
    list_display = ('id','nombres','apellidos','sexo','descripcion','carrera',)
    resource_class = CarreraResource

class DeporteMasculinoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre',)
    resource_class = DeporteMasculinoResource

class DeporteFemeninoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre',)
    resource_class = DeporteFemeninoResource

class DeporteAdmin(admin.ModelAdmin):
    search_fields = ['id','alumno','masculino','femenino']
    list_display = ('id','alumno','masculino','femenino',)
    resource_class = DeporteFemeninoResource




admin.site.register(Universidad,UniversidadAdmin)
admin.site.register(Facultad,FacultadAdmin)
admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(DeporteMasculino,DeporteMasculinoAdmin)
admin.site.register(DeporteFemenino,DeporteFemeninoAdmin)
admin.site.register(Deporte, DeporteAdmin)
