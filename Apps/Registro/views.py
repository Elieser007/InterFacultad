# from django.shortcuts import render
# from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
# from django.urls import reverse_lazy

# from .models import Universidad,Facultad
# from .forms import *



# class Registro(TemplateView):
#     template_name = "Administracion/Registro/registro.html"

# # Universidad
# class UniversidadView(ListView):
#     template_name = 'Administracion/Registro/universidad/universidad.html'
#     paginate_by= 10
#     context_object_name = 'universidad'
#     queryset = Universidad.objects.all()

# class CrearUniversidad(CreateView):
#     model = Universidad
#     form_class = UniversidadForm
#     template_name = 'Administracion/Registro/universidad/crear_universidad.html'
#     success_url = reverse_lazy('administracion:registro:universidad')

# class EditarUniversidad(UpdateView):
#     model = Universidad
#     form_class = UniversidadForm
#     template_name = 'Administracion/Registro/universidad/editar_universidad.html'
#     success_url = reverse_lazy('administracion:registro:universidad')
# class EliminarUniversidad(DeleteView):
#     model = Universidad
#     template_name = 'Administracion/Registro/universidad/eliminar_universidad.html'
#     success_url = reverse_lazy('administracion:registro:universidad')
    

# # Facultad
# class FacultadView(ListView):
#     template_name = 'Administracion/Registro/facultad/facultad.html'
#     paginate_by= 10
#     context_object_name = 'facultad'
#     queryset = Facultad.objects.all()

# class CrearFacultad(CreateView):
#     model = Facultad
#     form_class = FacultadForm
#     template_name = 'Administracion/Registro/facultad/crear_facultad.html'
#     success_url = reverse_lazy('administracion:registro:facultad')

# class EditarFacultad(UpdateView):
#     model = Facultad
#     form_class = FacultadForm
#     template_name = 'Administracion/Registro/facultad/editar_facultad.html'
#     success_url = reverse_lazy('administracion:registro:facultad')
# class EliminarFacultad(DeleteView):
#     model = Facultad
#     template_name = 'Administracion/Registro/facultad/eliminar_facultad.html'
#     success_url = reverse_lazy('administracion:registro:facultad')