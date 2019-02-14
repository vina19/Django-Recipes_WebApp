import requests

url = 'http://www.recipepuppy.com/api/'

def get_recipe_name(name):

	names = requests.get(url, {'title' : name}).json()
	return names['data']