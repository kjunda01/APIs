from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from django.shortcuts import render
from django.db import connection  # Importar a conexão com o banco de dados

def minha_view(request):
    contexto = {'chave': 'valor'}
    return render(request, 'index.html', contexto)

@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    connection.close()  # Fechar a conexão após o GET
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    connection.close()  # Fechar a conexão após o GET
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    connection.close()  # Fechar a conexão após o POST
    return Response(serializer.data)

@api_view(['PUT'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    connection.close()  # Fechar a conexão após o PUT
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    connection.close()  # Fechar a conexão após o DELETE
    return Response('User successfully deleted!')
