
from django.shortcuts import render
from django.views.decorators import cache


@cache.cache_page(12)
def index(request):
    context = {
        'count': range(1, 1001)
    }

    return render(request, 'cache.html', context)

