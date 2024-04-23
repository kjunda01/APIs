from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response('User successfully deleted!')


'''
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Inscricao
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import generics
from .models import Inscricao
from .serializers import InscricaoSerializer



class ListarInscricoes(generics.ListAPIView):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer


@csrf_exempt
def listar_inscricoes(request):
    inscricoes = Inscricao.objects.all()
    data = [{'id': inscricao.id, 'nome': inscricao.nome, 'email': inscricao.email} for inscricao in inscricoes]
    return JsonResponse(data, safe=False)


@csrf_exempt
def listar_criar_inscricoes(request):
    if request.method == 'GET':
        # Lógica para listar inscrições
        inscricoes = Inscricao.objects.all()
        data = [{'nome': inscricao.nome, 'email': inscricao.email} for inscricao in inscricoes]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        # Lógica para criar uma nova inscrição
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        if nome and email:
            inscricao = Inscricao.objects.create(nome=nome, email=email)
            return JsonResponse({'mensagem': 'Inscrição criada com sucesso!'}, status=201)
        else:
            return JsonResponse({'erro': 'Nome e email são obrigatórios'}, status=400)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])



@csrf_exempt
def atualizar_excluir_inscricao(request, inscricao_id):
    try:
        inscricao = Inscricao.objects.get(pk=inscricao_id)
    except Inscricao.DoesNotExist:
        return JsonResponse({'erro': 'A inscrição não existe'}, status=404)

    if request.method == 'PATCH':
        # Lógica para atualização aqui
        pass
    elif request.method == 'DELETE':
        inscricao.delete()
        return JsonResponse({'mensagem': 'Inscrição excluída com sucesso!'})
    else:
        return JsonResponse({'erro': 'Método HTTP não permitido'}, status=405)
    
def obter_inscricao(request, inscricao_id):
    try:
        inscricao = Inscricao.objects.get(pk=inscricao_id)
        data = {'nome': inscricao.nome, 'email': inscricao.email}
        return JsonResponse(data, safe=False)
    except Inscricao.DoesNotExist:
        return JsonResponse({'erro': 'Inscrição não encontrada'}, status=404)
    '''