from django.shortcuts import render


def description(request):
    context = {}
    TEMPLATE_NAME = 'about/description.html'
    return render(request, TEMPLATE_NAME, context=context)
