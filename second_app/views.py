from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def render_view(request):

    return render(request, 'index.html')

def view(request, name):
    print(request)
    print(name)
    return HttpResponse(name)

def another_view(request):

    return redirect('hello/')