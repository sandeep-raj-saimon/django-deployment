from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import HttpResponse

@api_view(['GET'])
@permission_classes([AllowAny,])
def index(request):
    print("server is accessible")
    dic={}
    dic["first_name"] = "sandeep"
    dic["last_name"] = "saimon"
    # return Response({"dic":dic})
    return HttpResponse("done")