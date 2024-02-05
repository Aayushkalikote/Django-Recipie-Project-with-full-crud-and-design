from django.shortcuts import render
from recipe.models import Recipe
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def recipe(request):
    queryselect=  Recipe.objects.all()  
    context = {'recipes':queryselect}
    return render(request, 'recipes.html',context)
def add_recipe(request):
    if request.method=="POST":
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_image=request.FILES.get('recipe_image')
        Recipe.objects.create(recipe_name=recipe_name,recipe_description=recipe_description,recipe_image=recipe_image)
        messages.success(request, "Recipe added successfully.")
    queryselect=  Recipe.objects.all()  
    context = {'recipes':queryselect}    
    return render(request,'add-recipes.html',context)
def delete_recipe(request,id):
    queryselect=Recipe.objects.get(id=id)
    queryselect.delete()
    messages.success(request, "Recipe Deleted successfully.")
    return redirect('/add_recipes')
