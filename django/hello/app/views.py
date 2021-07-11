from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse
from  app.models  import Article

def  hello_world(request):
    return HttpResponse("Hello World")


def content(request):
    all_ = Article.objects.all()
    return HttpResponse(all_)

