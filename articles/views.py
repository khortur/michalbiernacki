from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the articles index.")

def detail(request, article_id):
    return HttpResponse("You're looking at article %s." % article_id)