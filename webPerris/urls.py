
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='IND'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario,name='FORMU'),
    path('quien/',quienes_somos,name='QUIEN'),
    path('admin_perris/',admin_mascotas,name='ADM_PERRIS'),
    path('ficha/<id>/',ficha_mascota,name='FICH_MAS'),
    path('buscar_nombre/',buscar_nombre,name='BUSCAR_NOM'),
    path('buscar_palabra/',buscar_palabra_clave,name='BUSCAR_PAL'),
    path('filtro_cat/<id>/',fitro_categoria,name='FIL_CAT'),
    path('login/',login,name='LOGIN'),
    path('cerrar/',cerrar_sesion,name='CERRAR'),
    path('registro_colaborador/',registro,name='RC'),
]