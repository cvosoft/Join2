from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def contacts_view(request):
    if request.method == 'GET':
        return Response({"message": "hallo!!!"})
    if request.method == 'POST':
        try:
            msg = request.data['message']
            return Response({"message": msg}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def users_view(request):
    return Response({"message": "hallo!!!"})


@api_view(['GET'])
def tasks_view(request):
    return Response({"message": "hallo!!!"})
