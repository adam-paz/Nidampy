from rest_framework import serializers
from .models import Board
from .models import Topic
from .models import Post

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'description')