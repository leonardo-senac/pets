from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar_vacina/', cadastrar_vacina, name='cadastrar_vacina'),
    path('exibir_vacinas/', exibir_vacinas, name='exibir_vacinas'),
    path('editar_vacina/<int:id_vacina>/', editar_vacina, name='editar_vacina'),
    path('excluir_vacina/<int:id_vacina>/', excluir_vacina, name='excluir_vacina'),

    path('cadastrar_anuncio/', cadastrar_anuncio, name='cadastrar_anuncio'),
    path('exibir_anuncios/', exibir_anuncios, name='exibir_anuncios'),
    path('editar_anuncio/<int:id_anuncio>/', editar_anuncio, name='editar_anuncio'),
    path('excluir_anuncio/<int:id_anuncio>/', excluir_anuncio, name='excluir_anuncio'),
    path('pagina_anuncio/<int:id_anuncio>/', pagina_anuncio, name='pagina_anuncio'),
    path('vacina_anuncio/<int:id_anuncio>', vacina_anuncio, name='vacina_anuncio'),

    path('logar/', logar, name='logar'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('deslogar/', deslogar, name='deslogar'),

    path('anuncios_pessoais/', anuncios_pessoais, name='anuncios_pessoais'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)