from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', view=views.listar_medicos, name='listar_medicos'),
    path('consultas/nova/', view=views.criar_consulta, name='form_consulta'),
    path('consultas/<int:id>/', view=views.detalhes_consulta, name='detalhes_consulta'),
]