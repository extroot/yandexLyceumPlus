from django.shortcuts import render


def description(request):
    context = {}
    template = 'about/description.html'
    return render(request, template, context=context)
