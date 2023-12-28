from django.shortcuts import render, HttpResponse

# Create your views here.
def leaf (request):
    return HttpResponse ("This is a leaf page")