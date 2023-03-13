from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'title': 'My awesome Questions list',
        'questions': questions
    }
    return render(request, 'polls/index.html', context)

def jp(request):
    return HttpResponse("Hello jp, we are at the index")