from django.shortcuts import HttpResponse


def item_list(request):
    return HttpResponse('<h1>Список элементов</h1>')


def item_detail(request, id_product):
    return HttpResponse(f'<h1>Подробно элемент {id_product}</h1>')
