from .models import *
from .serializers import MedicoSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import re
from django.core.validators import RegexValidator



#Lista todos os médicos cadastrados
@api_view(['GET'])
def listar_medicos(request):
    medicos = Medico.objects.all()
    serializer = MedicoSerializer(medicos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#Formulário para agendar nova consulta
@api_view(['POST'])
def criar_consulta(request):
    serializer = MedicoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Exibe informações de uma consulta específica
@api_view(['GET'])
def detalhes_consulta(request):
    medico = get_object_or_404(Medico)
    serializer = MedicoSerializer(medico)
    return Response(serializer.data, status=status.HTTP_200_OK)







