import random

from django.shortcuts import render
from django.views.decorators import cache


@cache.cache_page(12)
def index(request):
    context = {
        'count': random.randint(1, 1000)
    }

    return render(request, 'cache_session_signals_middleware/cache.html', context)

