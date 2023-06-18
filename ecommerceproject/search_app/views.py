from django.shortcuts import render
# Create your views here.
from django.db.models import Q
from shop.models import Product


def SearchResult(request, q=None):
    query = None
    product = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        product = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'query': query,
        'product': product
    }

    return render(request, 'search.html', context)

