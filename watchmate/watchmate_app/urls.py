from django.urls import path, include
from watchmate_app.api.views import movie_list, movie_details
# from watchmate_app.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
   path('list/', movie_list, name='movie-list'),
   path('<int:pk>', movie_details, name='movie-details')
   # path('list/', MovieListAV.as_view(), name='movie-list'),
   # path('<int:pk>', MovieDetailAV.as_view(), name='movie-details')
]
#