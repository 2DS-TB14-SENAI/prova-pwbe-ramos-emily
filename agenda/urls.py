from django.urls import path
from . import views

urlpatterns = [
    path('api/servicos', view=views.listar_servicos, name='listar_servicos'),
    path('api/servicos', view=views.criar_servicos, name='criar_servicos'),
    path('api/servicos/<id>/', view=views.detalhes_servicos, name='detalhes_servicos'),
    path('api/agendamentos', view=views.listar_agendamementos, name='listar_agenda'),
    path('api/agendamentos', view=views.criar_agendamentos, name='criar_agenda'),
    path('api/agendamentos/<id>/', view=views.detalhes_agendamentos, name='detalhes_agenda'),
]