from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Board
from rest_framework import viewsets
from .serializers import BoardSerializer
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

def home(request):
    #boards = Board.objects.all()
    #return render(request, '../../client/public/index.html')
    #, {'boards': boards})
    
    boards = Board.objects.values()
    serializer_class = serializers.serialize

    

    #return HttpResponse(request, 'frontend/index.js', {'boards': boards})
    return JsonResponse({'boards':'boards'})

class BoardViewSet(viewsets.ModelViewSet, APIView):
    
    # def get_queryset(self):
    #     queryset = Board.objects.all().order_by('name')
    #     serializer = BoardSerializer(queryset, many=True)
    #     response = {"boards": serializer.data}    
    #     return Response(response, status=status.HTTP_200_OK)

    # queryset = Board.objects.all().order_by('name')
    serializer_class = BoardSerializer

    @action(detail=True, methods=['post'])
    def create_board(self, request, format=None):
        data = request.data
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            board = Board(**data)
            board.save()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        # queryset = Board.objects.all()
       
        board = self.request.query_params.get('board', None)
        queryset = Board.objects.filter(name=board)
        # if board is not None:
        #     queryset = queryset.filter(name=board)
        return queryset