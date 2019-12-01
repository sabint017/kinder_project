from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)


def index(request):
    return render(request, 'index.html')


def queries(request):
    return render(request, 'queries.html')


def dev(request):
    return render(request, 'dev.html')


def services(request):
    return render(request, 'services.html')


# Create your views here.
