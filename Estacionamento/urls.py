"""Estacionamento URL Configuration

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
from django.urls import path
from Site import views as Site
from Login import views as Login


urlpatterns = [
    path('admin/', admin.site.urls),

    # App Site:
    path('', Site.index, name="site-index"),
    path('sobre/', Site.sobre, name="site-sobre"),
    path('preco/', Site.preco, name="site-preco"),
    path('suporte/', Site.suporte, name="site-suporte"),
    path('carrinho/', Site.carrinho, name="site-carrinho"),

    # App Login:
    path('Login/', Login.index, name="login-index"),
    path('dashboard/', Login.dashboard, name="login-dashboard"),
    path('icons/', Login.icons, name="login-icons"),
    path('map/', Login.map, name="login-map"),
    path('notifications/', Login.notifications, name="login-notifications"),
    path('tables/', Login.tables, name="login-tables"),
    path('typography/', Login.typography, name="login-typography"),
    path('user/', Login.user, name="login-user"),




    #So ativada quando vou fazer testes
    #path("teste/", Site.teste, name="teste"),
]
