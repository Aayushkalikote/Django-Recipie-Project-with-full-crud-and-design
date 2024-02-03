from django.contrib import admin
from django.urls import path
from django.urls import path,include
from recipe import views

urlpatterns = [
    path('', views.recipe,name='recipe'),
    path('add_recipes', views.add_recipe, name='add_recipes'),
]
