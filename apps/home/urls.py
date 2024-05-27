# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024- present Suavecitos.corp
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('get-token-publico', views.getTokenPublico, name='get-token-publico'),
    path('set-firma', views.guardar_firma, name='set-firma'),
    path('mostrar_firma', views.mostrar_firma, name='mostrar_firma'),
    path('get-perfiles', views.getPerfiles, name='get-perfiles'),
    path('set-perfil', views.setPerfil, name='set-perfil'),
    path('get-permisos', views.getPermisos, name='get-permisos'),
    path('get-usuarios', views.getUsuarios, name='get-usuarios'),
    path('set-permiso', views.setPermiso, name='set-permiso'),
    path('get-perfil', views.getPerfil, name='get-perfil'),
    path('set-perfil-usuario', views.setPerfilUsuario, name='set-perfil-usuario'),
    path('get-municipio-xdepartamento', views.getMunicipioXDepartamento, name='get-municipio-xdepartamento'),
    path('get-pdv-xmunicipio', views.getPdvXMunicipio, name='get-pdv-xmunicipio'),
    path('get-usuarios-opt', views.getUsuariosOpt, name='get-usuarios-opt'),
    path('get-pdv', views.getPdv, name='get-pdv'),
    path('set-pdv', views.setPdv, name='set-pdv'),
    path('get-rutas', views.getRutas, name='get-rutas'),
    path('set-rutas', views.setRutas, name='set-rutas'),
    
    
    
    path('status-session',views.status_session, name='status-session'),
    path('login-app',views.login_app, name='login-app'),
    
    
    re_path(r'public\/*', views.publicLink, name='public-link'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
