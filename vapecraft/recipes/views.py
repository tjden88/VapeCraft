from django.shortcuts import render
from . import models

def index(request):
    all_recipes = models.Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': all_recipes})