from django.contrib import admin

# Register your models here.

from .models import Category, Ingredient, Cocktail, CocktailIngredient

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Cocktail)
admin.site.register(CocktailIngredient)
