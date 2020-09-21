from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Board
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .serializers import BoardSerializer
import json
from django.core import serializers

def home(request):
    #boards = Board.objects.all()
    #return render(request, '../../client/public/index.html')
    #, {'boards': boards})
    
    boards = Board.objects.all()
    serializer_class = serializers.serialize('json', boards)

    

    return render(request, 'home.html', {'boards': boards})
    