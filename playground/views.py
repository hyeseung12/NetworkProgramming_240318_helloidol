from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    return HttpResponse("Hello World")

def say_hello_html(request):
    return render(request, 'playground/hello.html', {'name': '지우야', 'greeting': '안녀엉~'})

def say_bye_html(request):
    context = {
        'singer': '박화요비',
        'title': '그런 일은',
    }
    return render(request, 'playground/bye.html', context=context)