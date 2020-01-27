from django.contrib import admin
from django.urls import path
from pagina import views


urlpatterns = [
    path('ongs/lista/', views.lista_ongs),
    path('ongs/', views.cadastrar_ong),
    path('lista/', views.pessoas),
    path('admin/', admin.site.urls),
    path('', views.index),
    path('pet/cadastrar', views.cadastrar_pet),
    path('login', views.login),
]
