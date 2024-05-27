from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'site_title': 'Princiapal'
    }
    return render(request, 'project/index.html', context)