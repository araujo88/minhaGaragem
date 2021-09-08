from django.urls import path, include
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('usuario/', include('pessoa.urls')),
    path('garagem/', include('garagem.urls')),
    path('meu-perfil/', views.perfil, name='perfil'),
]
