from django.shortcuts import render


def index(request):
    return render(request, 'about/index.html')


def resume(request):
    return render(request, 'about/resume.html')


def timeline(request):
    return render(request, 'about/index.html')
