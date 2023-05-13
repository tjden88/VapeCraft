
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='recipes'),
    path('recipe/<int:pk>/', views.RecipeDetails.as_view(), name='recipe-details'),
]
