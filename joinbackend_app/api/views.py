from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def contacts_view(request):
    if request.method == 'GET':
        return Response({"message": "hallo!!!"})
    if request.method == 'POST':
        try:
            msg = request.data['message']
            return Response({"message": msg}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


@api_view(['GET', 'POST'])
def users_view(request):
    if request.method == 'GET':
        return Response({"message": "hallo!!!"})
    if request.method == 'POST':
        pass


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def tasks_view(request):
    if request.method == 'GET':
        return Response({"message": "hallo!!!"})
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def subtasks_view(request):
    if request.method == 'GET':
        return Response({"message": "hallo!!!"})
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass
