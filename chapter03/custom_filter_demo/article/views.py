from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from datetime import datetime


def index(request):
    context = {
        'value': 'tom',
        'my_time': datetime(year=2020, month=11, day=14, hour=18, minute=27, second=30)
    }
    return render(request, 'index.html', context=context)
