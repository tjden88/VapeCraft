from django.shortcuts import render
from django.views.generic import DetailView
from . import models

def index(request):
    all_recipes = models.Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': all_recipes})

class RecipeDetails(DetailView):
    model = models.Recipe
    template_name = 'recipes/details.html'
    