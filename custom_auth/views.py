from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    phone = request.data.get('phone')
    address= request.data.get('address')
    birth_date = request.data.get('birth_date')

    if not username or not password or not phone or not address or not birth_date:
        return Response({'ERRO' : 'Informações Insuficientes'}, status=status.HTTP_400_BAD_REQUEST)
    
    if CustomUser.objects.filter(username = username).exists():
        return Response({"ERRO" : 'Username já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = CustomUser.objects.create_user(
        username = username,
        password = password,
        phone = phone,
        address = address,
        birth_date = birth_date
    )
    return Response({'Criado' : f'Usuário {usuario} criado'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar(request):
    username = request.data.get('username')
    password = request.data.get('password')

    usuario = authenticate(username=username, password=password)

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'access' : str(refresh.access_token),
            'refresh' : str(refresh),
        }, status=status.HTTP_200_OK)

    else:
        return Response({'Erro' : 'Usuario ou senha inválido'}, status=status.HTTP_401_UNAUTHORIZED)