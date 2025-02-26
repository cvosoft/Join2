from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from .serializers import ContactSerializer
from joinbackend_app.models import Contact


class ContactsView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Contact.objects.all()
    serializer = ContactSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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


@api_view(['GET', 'DELETE', 'PUT'])
def contacts_single_view(request, pk):
    if request.method == 'GET':
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    if request.method == 'PUT':
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(
            contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(contact)
        contact.delete()
        return Response(serializer.data)


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
