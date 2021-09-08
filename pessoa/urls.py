from django.urls import path
from . import views

urlpatterns = [
    path('', views.pessoas, name='pessoas'),
    path('pessoa/<str:pk>/', views.pessoa, name="pessoa"),
    path('criar-usuario/', views.criarUsuario, name="criar-usuario"),
    path('editar-usuario/<str:pk>/', views.editarUsuario, name="editar-usuario"),
    path('deletar-usuario/<str:pk>/', views.deletarUsuario, name="deletar-usuario") 
]