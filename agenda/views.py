from .models import *
from .serializers import ServicoSerializer, AgendamentoSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import re
from django.core.validators import RegexValidator


#Lista todos os servicos disponiveis
@api_view(['GET'])
def listar_servicos(request):
    servicos = Servico.objects.all()
    serializer = ServicoSerializer(servicos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#Formulário para agendar novo servico
@api_view(['POST'])
def criar_servicos(request):
    serializer = ServicoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Detalhes de um serviço específico
@api_view(['GET'])
def detalhes_servicos(request):
    servico = get_object_or_404(Servico)
    serializer = ServicoSerializer(servico)
    return Response(serializer.data, status=status.HTTP_200_OK)







#Lista todos os agendamentos
@api_view(['GET'])
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    serializer = AgendamentoSerializer(agendamentos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Cria novo agendamento
@api_view(['POST'])
def criar_agendamentos(request):
    serializer = AgendamentoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Detalhes de um agendamento
@api_view(['GET'])
def detalhes_agendamentos(request):
    agendamento = get_object_or_404(Agendamento)
    serializer = AgendamentoSerializer(agendamento)
    return Response(serializer.data, status=status.HTTP_200_OK)
