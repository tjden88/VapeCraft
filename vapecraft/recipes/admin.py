from django import forms
from django.contrib import admin
from . import models

class RecipesAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating' , 'created', 'modified')
    list_display_links = ('name',)
    search_fields = ('name',)
        
        
admin.site.register(models.Recipe, RecipesAdmin)