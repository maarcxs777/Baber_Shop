from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('', include('agendamento.urls')),
    path('', include('produtos.urls')),
    path('', include('contatos.urls')),
    path('', include('dados.urls')),
]
