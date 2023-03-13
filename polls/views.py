from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world, we are at the index")

def jp(request):
    return HttpResponse("Hello jp, we are at the index")