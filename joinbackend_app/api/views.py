from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def contacts_view(request):
    return Response({"message": "hallo!!!"})


@api_view(['GET'])
def users_view(request):
    return Response({"message": "hallo!!!"})


@api_view(['GET'])
def tasks_view(request):
    return Response({"message": "hallo!!!"})
