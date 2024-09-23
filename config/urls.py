from django.contrib import admin
from django.urls import include, path
from django.views.generic import *
import app.views as views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.IndexView.as_view(), name='index'),
    path('hangmangame/', views.HangmanView.as_view(), name='jogo'),
    path('senha/', views.SenhaView.as_view(), name='senha'),
    path('deletePalavra/<int:id>/', views.DeletePalavra.as_view(), name='deletePalavra'),
    path('deleteUsuario/<int:id>/', views.DeleteUsuario.as_view(), name='deleteUsuario'),
    path('deleteJogo/<int:id>/', views.DeleteJogo.as_view(), name='deleteJogo'),
    path('lista/', views.ListaView.as_view(), name='lista'),
    path('inserir/', views.InserirView.as_view(), name='inserir')
]