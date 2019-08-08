from django.shortcuts import render, redirect
from .models import Question
# Create your views here.

def new(request):
    return render(request, 'new.html')

def create(request):
    user = request.GET.get('user')
    title = request.GET.get('title')
    content = request.GET.get('content')

    question = Question()
    quest.user = user
    question.title = title
    question.content = content
    question.save()

    return redirect('/questions/')