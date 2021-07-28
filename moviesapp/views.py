  
from django.db import models
from django.shortcuts import render
from rest_framework import generics

from .models import Movies
from .serializer import MoviesSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class MoviesListView(generics.ListCreateAPIView):    
    serializer_class = MoviesSerializer
    queryset = Movies.objects.all()

class MoviesDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoviesSerializer
    queryset = Movies.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)