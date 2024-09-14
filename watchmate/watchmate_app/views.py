#from django.shortcuts import render
#from watchmate_app.models import Movie
#from django.http import JsonResponse
# Create your views here.
#def movie_list(request):
#    movies = Movie.objects.all()#extracted data in a queryset and convert into a dictionary
   #convert into a list
 #   data ={'movies': list(movies.values())}# convert python dictionary into a json data
  #  return JsonResponse(data)


#def movie_details(request,pk):
 #   movie = Movie.objects.get(pk=pk)
  #  data ={
       # 'name':movie.name,
       # 'decscription':movie.description,
      #  'active':movie.active
    #return JsonResponse(data)
