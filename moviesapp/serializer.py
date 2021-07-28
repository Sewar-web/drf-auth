  
from rest_framework import serializers

from .models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'movie', 'desc', 'director', 'watcher' , 'rank')
        model = Movies