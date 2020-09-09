from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

def home(request):
    #boards = Board.objects.all()
    #return render(request, '../../client/public/index.html')
    #, {'boards': boards})
    
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})