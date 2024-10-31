"""
URL configuration for audiometria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('authentication/', include('authentication.urls')),
    path('exame_audiometria/', include('exame_audiometria.urls')),
    path('paciente/', include('paciente.urls')),
    path('reflexo_acustico/', include('reflexo_acustico.urls')),
    path('timpanograma/', include('timpanograma.urls')),
    path('classificacao_iprf/', include('classificacao_iprf.urls')),
    path('configuracao_audiometrica/', include('configuracao_audiometrica.urls')),
    path('grau_perda/', include('grau_perda.urls')),
    path('tipo_perda_auditiva/', include('tipo_perda_auditiva.urls')),
    path('admin/', admin.site.urls),
]
