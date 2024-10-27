from django.urls import path
from . import views

urlpatterns = [
    path('contatos/', views.contatos, name='contatos')
]
