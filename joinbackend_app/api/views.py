from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer
from joinbackend_app.models import Contact


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def contacts_view(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

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
