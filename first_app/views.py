from django.shortcuts import render, HttpResponse

def hellodjango(request):
    return HttpResponse('Hello Django')

# Create your views here.
