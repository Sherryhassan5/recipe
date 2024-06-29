from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        if not User.objects.filter(username = username).exists():
            messages.info(request, 'Username does not exist')
            return redirect(login_page)
        user = authenticate(username = username,password = password)
        if user is None:
            messages.info(request,'Invalid Credentials')
            return redirect(login_page)
        login(request, user)
        return redirect(reverse('home'))
    return render(request, 'accounts/login.html')

def logout_page(request):
    logout(request)
    return redirect(reverse('home'))

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        
        
        user1 = User.objects.filter(username = username)
        if user1.exists():
            messages.info(request, 'Username already exist')
            return redirect(register)
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save()
        print('created')
        login(request , user)
        return redirect(reverse('home'))
    return render(request, 'accounts/register.html')


def profile(request,id):
    user = User.objects.get(id = id)
    print(user)
    context = {'bnda':user}
    return render(request, 'accounts/profile.html', context)