from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchmate_app.models import Movie
from watchmate_app.api.serializers import MovieSerializer

#   using  a clase based viesw
class MovieListAV(APIView):
    def get(self, request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        else:
            return Response(serializer.errors)
class MovieDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error' :'Movie not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    def put(self,request,pk):
        movie =  Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status)
        

# THE COMMENTED CODES BELOW IS FOR  A FUCTION BASED VIEWS WHICH IS USED TO VIEW THE DATABASE
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()    
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method=='GET':    
    #     try:
    #         movie = Movie.objects.get(pk=pk)
    #     except Movie.DoesNotExist:
    #         return Response({'error': 'Movie Not Found'},status=status.HTTP_404_NOT_FOUND)
    #     serializer = MovieSerializer(movie)
    #     return Response(serializer.data)
    # #updating individual movie details and storing into a database
    # if request.method =='PUT':
    #     movie = Movie.objects.get(pk=pk)
    #     serializer = MovieSerializer(movie, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.error)
    # if request.method == 'DELETE':
    #     try:
    #         movie = Movie.objects.get(pk=pk)
    #     except Movie.DoesNotExist:
    #         return Response({'error': 'Movie Not Found in the database'},status=status.HTTP_404_NOT_FOUND)
    #     movie.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
        
    