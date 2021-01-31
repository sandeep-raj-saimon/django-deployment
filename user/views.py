from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from .models import *
import json
@api_view(['GET'])
@permission_classes([AllowAny,])
def index(request):
    try:
        print("server is accessible")
        
        return HttpResponse("<h2> You are now connected to server</h2>")
    except Exception as error:
        return HttpResponse("<h2> Some error occured </h2>"+str(oount))

@api_view(['GET'])
@permission_classes([AllowAny])
def createUser(request):
    try:
        name = request.GET.get("name")
        print(name)
        user = User()
        user.name = name
        user.save()
        print("object is created")
        count = User.objects.count()
        return HttpResponse("<h2> count of records is </h2>"+str(count))
    except Exception as error:
        return HttpResponse("<h2> some error occured in the logic </h2>" +str(error))

@api_view(['GET'])
@permission_classes([AllowAny])
def getAll(request):
    try:
        user_data = User.objects.all()
        output={}
        for user in user_data:
            
            output[str(user.id)]=user.name

        return HttpResponse("<h2> User in DB are </h2>"+json.dumps(output))
    except Exception as error:
        return HttpResponse("<h2> Something went wrong </h2>"+str(error))
    