from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'site_title': 'Princiapal'
    }
    return render(request, 'project/index.html', context)

def create_view(request):
    context = {
        'site_title': 'Criar'
    }
    return render(request, 'project/create.html', context)

def login_view(request):
    context = {
        'site_title': 'Criar'
    }
    return render(request, 'project/login.html', context)