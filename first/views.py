from django.shortcuts import render





def index(request):
    return render(request, 'index.html')


def queries(request):
    return render(request, 'queries.html')


def dev(request):
    return render(request, 'dev.html')


def services(request):
    return render(request, 'services.html')

def signup(request):
    return render(request, 'signup.html')




# Create your views here.
