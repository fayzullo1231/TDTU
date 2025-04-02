import json

from django.shortcuts import render
from .models import Students, News, Department, Invites

def home_views(request):
    news = News.objects.all()
    students = Students.objects.all()

    context = {
        'news': news,
        'students': students,
    }
    return render(request, 'home.html', context)

def news_views(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'news.html', context)

def reception_online(request):
    if request.method == "POST":
        data = request.body
        obj = Invites.objects.create(full_name=request.POST['fullname'], email=request.POST['email'],
                               phone=request.POST['raqam'], location=request.POST['manzil'],
                               city=request.POST['viloyat'], district=request.POST['tuman'],
                               age=request.POST['yoshingiz'], message=request.POST['xabar'])
        obj.save()
        print(request.body)
        # Invites.objects.create()
    return render(request, 'reception_online.html')