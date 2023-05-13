from django.views.generic import DetailView, ListView
from . import models


class RecipeDetails(DetailView):
    model = models.Recipe
    template_name = 'recipes/details.html'


class RecipeList(ListView):
    model = models.Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'
    # extra_context = {'title': 'Главная'}


    #def get_queryset(self):
    #    return models.Recipe.objects.filter(is_published=True)
    