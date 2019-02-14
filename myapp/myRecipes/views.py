from django.shortcuts import render
from . import recipes_api

#Creating the home page by returning
#to render with request argument and home.html 
#templates within YaMooRecipes subdirectory.  
def home(request):
	return render(request, 'myRecipes/home.html')

#Creating the recipes page by returning
#to render with request argument and recipes.html
#templates within YaMooRecipes subdirectory. 
def recipes(request):
	return render(request, 'myRecipes/recipes.html', 
 		{'title' : 'Recipes'})

def get_recipe_name(request):
	name = request.GET.get('name', 'YaMoo')
	recipe_name = recipes_api.get_recipe_name(name)
	return render(request, 'myRecipes/recipe_name.html', {'names' : names})