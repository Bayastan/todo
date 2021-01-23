from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("hello world")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("Test page 2")

def third(request):
    return HttpResponse("This is page3")