from django.contrib import admin
from . import models

class RecipesAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating' , 'created', 'modified')
    list_display_links = ('name',)
    list_filter = ('name',)

admin.site.register(models.Recipe, RecipesAdmin)