from django.urls import path
from . import views

urlpatterns = [
    path('', views.veiculos, name='veiculos'),
    path('veiculo/<str:pk>/', views.veiculo, name="veiculo"),
    path('criar-veiculo/', views.criarVeiculo, name="criar-veiculo"),
    path('editar-veiculo/<str:pk>/', views.editarVeiculo, name="editar-veiculo"),
    path('deletar-veiculo/<str:pk>/', views.deletarVeiculo, name="deletar-veiculo") 
]