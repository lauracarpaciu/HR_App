from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    context = {'title':'Articles'}
    return render(request, 'kb/home.html',context)

def about(request):
    # return HttpResponse("<h1> About Knowledge base </h1>")
    context = {'title':'About'}
    return render(request, 'kb/about.html',context)