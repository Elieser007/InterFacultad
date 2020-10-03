"""InterFacultad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.urls import path, include
# from django.contrib.auth.decorators import login_required

# from Apps.Registro.views import *

# urlpatterns = [
    # Universidad
    # path('universidad/', login_required(UniversidadView.as_view()), name="universidad"),
    # path('crear_universidad/', login_required(CrearUniversidad.as_view()), name="crear_universidad"),
    # path('editar_universidad/<int:pk>', login_required(EditarUniversidad.as_view()), name="editar_universidad"),
    # path('eliminar_universidad/<int:pk>', login_required(EliminarUniversidad.as_view()), name="eliminar_universidad"),
    # # Facultad
    # path('facultad/', login_required(FacultadView.as_view()), name="facultad"),
    # path('crear_facultad/', login_required(CrearFacultad.as_view()), name="crear_facultad"),
    # path('editar_facultad/<int:pk>', login_required(EditarFacultad.as_view()), name="editar_facultad"),
    # path('eliminar_facultad/<int:pk>', login_required(EliminarFacultad.as_view()), name="eliminar_facultad"),
# ]