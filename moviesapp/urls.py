from django.urls import path

from .views import MoviesListView, MoviesDetailsView

urlpatterns = [
    path('', MoviesListView.as_view(), name='movie_api'), 
    path('<int:pk>', MoviesDetailsView.as_view(), name='movie_details_api'), 
]