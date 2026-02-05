from sys import api_version
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
# Create your views her
def getRoutes(request):
    routes = [
        
        '/api/v1/projects/',
        '/api/v1/projects/<id>/', 
       
        '/api/v1/projects/create/',
        '/api/v1/projects/<id>/task/create/',
        
        '/api/v1/users',
        '/api/v1/users/create/',
    ]
    
    return JsonResponse('routes', safe=False)


@api_view(['GET'])
def getV1(request):
    return Response('API V1') 
