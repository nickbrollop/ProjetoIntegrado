"""site_cartelas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path( '/', TemplateView.as_view(template_name='index.html')),
    path("accounts/",include("django.contrib.auth.urls")),
    path ('RecandoDaCompaixao/PaginaInicial/', TemplateView.as_view( template_name ='home_page.html') ),
    path ('RecandoDaCompaixao/QuemSomos/', TemplateView.as_view( template_name ='quem_somos.html') ),
    path ('RecandoDaCompaixao/Contato/', TemplateView.as_view( template_name ='contato.html') ),
    path ('RecandoDaCompaixao/Informacional/', TemplateView.as_view( template_name ='informacional.html') ),
    path ('RecandoDaCompaixao/Doacao/', TemplateView.as_view( template_name ='doacao.html') ),
]
