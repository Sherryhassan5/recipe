from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('addrecipe/', views.addrecipe, name='addrecipe'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/deleterecipe/<id>/', views.deleterecipe, name='deleterecipe'),
    path('recipes/editrecipe/<id>/', views.editrecipe, name='editrecipe'),
    path('recipe_detail/<id>/', views.recipedetail, name='recipe_detail'),
    path('search_recipe/', views.searchrecipe, name='search_recipe'),    
]
