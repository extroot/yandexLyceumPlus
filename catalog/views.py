from django.shortcuts import render


def item_list(request):
    context = {}
    return render(request, 'catalog/item_list.html', context)


def item_detail(request, id_product):
    context = {
        "id_product": id_product
    }
    return render(request, 'catalog/item_detail.html', context)
