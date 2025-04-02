
from django.shortcuts import render

def home_views(request):
    return render(request, 'home.html')

def news_views(request):
    return render(request, 'news.html')

def reception_online(request):
    return render(request, 'reception_online.html')