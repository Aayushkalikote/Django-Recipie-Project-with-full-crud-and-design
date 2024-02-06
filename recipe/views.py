from django.shortcuts import render
from recipe.models import Recipe
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def recipe(request):
    queryselect=  Recipe.objects.all()  
    context = {'recipes':queryselect}
    return render(request, 'recipes.html',context)
def view_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    context = {'recipe':queryset}
    return render(request,'view-recipe.html',context)
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
def update_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        recipe_image=request.FILES.get('recipe_image')
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')

        queryset.recipe_name=recipe_name
        queryset.recipe_description=recipe_description
        
        if recipe_image:
            queryset.recipe_image=recipe_image
        queryset.save()
        messages.success(request, "Recipe Updated successfully.")
        return redirect('/')
    context = {'recipe':queryset}
    return render(request,'update-recipe.html',context)

def delete_recipe(request,id):
    queryselect=Recipe.objects.get(id=id)
    queryselect.delete()
    messages.success(request, "Recipe Deleted successfully.")
    return redirect('/add_recipes')
