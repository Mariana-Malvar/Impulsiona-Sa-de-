from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro_voluntario, name='home'),
    path('lista/', views.lista_voluntarios, name='lista'),
    path('excluir/<int:id>/', views.excluir_voluntario, name='excluir'),
]