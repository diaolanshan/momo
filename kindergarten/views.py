from django.shortcuts import render
from kindergarten import config
import random


# Create your views here.
def create():
    result = []
    for count in range(0, config.COUNT):
        first = int(round(config.MAXIMUM * random.random()))
        second = int(round(config.MAXIMUM * random.random()))
        operator = config.OPERATOR[int(round(random.random()*10-1))//5]
        result.append([first, operator, second])

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

create()
