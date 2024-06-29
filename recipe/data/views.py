from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    
    return render(request, 'data/home.html')

@login_required
def addrecipe(request):
    if request.method == 'POST':
        data = request.POST
        recipe_img = request.FILES.get('recipe-img')
        user = request.user
        recipe_title =  data.get('recipe-title')
        recipe_desc = data.get('desc')
        
        recipe.objects.create(
         user = user,
         recipe_title = recipe_title,
         recipe_description = recipe_desc,
         recipe_img = recipe_img,  
        )
        return redirect(recipes)
    
    return render(request, 'data/addrecipe.html')

def recipes(request):
    query_set = recipe.objects.all()
    print(query_set)
    context = {'recipes': query_set}
    return render(request, 'data/recipes.html', context)

@login_required
def editrecipe(request, id):
    recipe_to_edit = recipe.objects.get(id = id)
    print(recipe_to_edit)
    if request.user.id != recipe_to_edit.user.id:
        messages.info(request, "You are not authorized for this action")
        return redirect(recipes)
    if request.method == 'POST':
        data = request.POST
        recipe_img = request.FILES.get('recipe-img')
        recipe_title =  data.get('recipe-title')
        recipe_desc = data.get('desc')
        recipe_to_edit.recipe_title = recipe_title
        recipe_to_edit.recipe_description = recipe_desc
        if recipe_img:
            recipe_to_edit.recipe_img = recipe_img
            
        recipe_to_edit.save()
        return redirect(recipes)
    context = {'recipe':recipe_to_edit}
    return render(request, 'data/editrecipe.html',context)

@login_required
def deleterecipe(request, id):
    recipe_to_dlt = recipe.objects.get(id = id)
    if request.user.id != recipe_to_dlt.user.id:
        messages.info(request, "You are not authorized for this action")
        return redirect(recipes)
    print(recipe_to_dlt)
    recipe_to_dlt.delete()
    messages.info(request, 'The item is deleted')
    return redirect(recipes)



def recipedetail(request, id):
    recipe_to_show = recipe.objects.get(id = id)
    context = {'recipi':recipe_to_show}
    return render(request, 'data/recipe_detail.html',context)

def searchrecipe(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        recipe_to_search = data.get('recipe_to_search')
        print(recipe_to_search)
        recipi = recipe.objects.filter(recipe_title__icontains = recipe_to_search)
        context = {'recipes':recipi}

    return render(request, 'data/recipes.html', context)