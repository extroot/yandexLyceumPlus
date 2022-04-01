from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'homepage/home.html', context=context)
