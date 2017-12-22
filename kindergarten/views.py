from django.shortcuts import render
from kindergarten import config
import random


# Create your views here.
def create(request):
    result = []
    for count in range(0, config.COUNT):
        first = int(round(config.MAXIMUM * random.random()))
        second = int(round(config.MAXIMUM * random.random()))
        operator = config.OPERATOR[int(round(random.random()*10-1))//5]
        if operator == '-':
            if second > first:
                result.append([second, operator, first])
                continue
        result.append([first, operator, second])
    ctx = {}
    ctx['items'] = result
    return render(request, 'hello.html', ctx)


def verify(request):
    pass


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
