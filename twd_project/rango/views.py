from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context = context_dict)

def about(request):
    context_dict = {'boldmessage': "Rango says here is the about page"}
    return render(request, 'rango/about.html', context=context_dict)

