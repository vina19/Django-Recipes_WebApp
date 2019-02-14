#importing the path from django.urls.
from django.urls import path
#importing views.py module to the urls.py.
from . import views

urlpatterns = [
	#Show the path which user will see 
	#which is the home view of httpresponse from views.py
	#and the name of the path which is YaMoo-home.
    path('', views.home, name='YaMoo-home'),

    #Display recipes page from the views.py that connect to recipes.html.
    #Named it as YaMoo-recipes.
    path('recipes/', views.recipes, name='YaMoo-recipes'),

  	path('getrecipes/', views.get_recipe_name, name='get_recipe'),




]