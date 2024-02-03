from django.shortcuts import render
from recipe.models import Recipe
from django.contrib import messages
# Create your views here.
def recipe(request):
    return render(request, 'recipes.html')
def add_recipe(request):
    if request.method=="POST":
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_image=request.FILES.get('recipe_image')
        Recipe.objects.create(recipe_name=recipe_name,recipe_description=recipe_description,recipe_image=recipe_image)
        messages.success(request, "Recipe added successfully.")
    return render(request,'add-recipes.html')