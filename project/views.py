from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from project.forms import RegisterForm

def index(request):
    context = {
        'site_title': 'Princiapal'
    }
    return render(request, 'project/index.html', context)

def create_view(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('sales:index')

    context = {
        'site_title': 'Criar',
        'title_form': 'Cadastrar',
        'form': form
    }
    return render(request, 'project/create.html', context)

def login_view(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('sales:index')

    context = {
        'site_title': 'Login',
        'title_form': 'Login',
        'form': form
    }
    return render(request, 'project/login.html', context)