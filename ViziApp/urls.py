"""
URL configuration for ViziApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('', views.inicial, name='inicial'),

    path('cadastrar-servico/', views.cadastrar_servico, name='cadastrar_servico'),
    
    
    path('servicos/', views.listar_servicos, name='listar_servicos'),
    
    
    path('viziapp/', views.listar_categoria, name='listar_categoria'),
    
    
    path('servico/<int:servico_id>/', views.detalhe_servico, name='detalhe_servico'),
    
    
    path('prestadores/', views.listar_prestadores, name='listar_prestadores'),
    path('editar_prestador/<int:id>/', views.editar_prestador, name='editar_prestador'),
]
