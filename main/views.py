from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html', {})


def home2(request):
    return render(request, 'main/home2.html', {})
