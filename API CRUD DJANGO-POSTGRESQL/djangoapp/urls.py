from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path ('create/', views.addUser),
    path ('read/<str:pk>', views.getUser),
    path ('update/<str:pk>', views.updateUser),
    path ('delete/<str:pk>', views.deleteUser),
]



'''
from django.urls import path
from .views import atualizar_excluir_inscricao, obter_inscricao, listar_criar_inscricoes

urlpatterns = [
    path('inscricoes/', listar_criar_inscricoes, name='listar_criar_inscricoes'),
    path('inscricoes/<int:inscricao_id>/', obter_inscricao, name='obter_inscricao'),
    path('inscricoes/<int:inscricao_id>/', atualizar_excluir_inscricao, name='atualizar_excluir_inscricao'),
]

'''
