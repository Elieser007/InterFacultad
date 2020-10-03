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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# from Apps.Registro.views import Registro
from Apps.Administracion.views import Administracion
from Apps.Login.views import Login, logout

urlpatterns = [
    path('accounts/', admin.site.urls, name='login'),
    path('', include('Apps.Pagina.urls')),
    # path('administracion/', login_required(Administracion.as_view()), name="administracion"),
    # path('administracion/', include(('Apps.Administracion.urls', 'administracion'))),
    # path('accounts/login/', Login.as_view(), name='login'),
    # path('logout/', login_required(logout), name='logout'),
    path('', include('pwa.urls')),
]

