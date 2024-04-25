from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path ('create', views.addUser),
    path ('read/<str:pk>', views.getUser),
    path ('update/<str:pk>', views.updateUser),
    path ('delete/<str:pk>', views.deleteUser),
    path('', TemplateView.as_view(template_name='index.html')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


'''
from django.urls import path
from .views import atualizar_excluir_inscricao, obter_inscricao, listar_criar_inscricoes

urlpatterns = [
    path('inscricoes/', listar_criar_inscricoes, name='listar_criar_inscricoes'),
    path('inscricoes/<int:inscricao_id>/', obter_inscricao, name='obter_inscricao'),
    path('inscricoes/<int:inscricao_id>/', atualizar_excluir_inscricao, name='atualizar_excluir_inscricao'),
]

'''
