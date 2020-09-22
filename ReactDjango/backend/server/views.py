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
    
    boards = Board.objects.values()
    serializer_class = serializers.serialize

    

    #return HttpResponse(request, 'frontend/index.js', {'boards': boards})
    return JsonResponse({'boards':'boards'})

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all().order_by('name')
    serializer_class = BoardSerializer
    