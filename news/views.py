from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.
def home1(request):
    categorys=Category.objects.all()
    region1=Region.objects.all()[0]
    regions=Region.objects.all()[1:]
    latestall=News.objects.order_by("-created_at")[:5]
    latest=News.objects.order_by("-created_at")[1:5]
    latest6=News.objects.order_by("-created_at")[6:9]
    latest1=News.objects.order_by("-created_at")[0]
    news=News.objects.all()
    context={
        "categorys":categorys,
        'news':news,
        'latest':latest,
        "regions":regions,
        'latestall':latestall,
        "region1":region1,
        "region1":region1,
        'latest1':latest1,
        'latest6':latest6,
    }
    return render(request,"home.html",context)

def category_news(request,slug):
    categorys=Category.objects.all()
    region1=Region.objects.all()[0]
    regions=Region.objects.all()[1:]
    category=Category.objects.get(slug=slug)
    latestall=News.objects.filter(category=category).order_by("-created_at")[:5]
    latest=News.objects.filter(category=category).order_by("-created_at")[1:5]
    latest6=News.objects.filter(category=category).order_by("-created_at")[6:9]
    latest1=News.objects.filter(category=category).order_by("-created_at").first()
    context={
    "categorys":categorys,
    "category":category,
    'latest':latest,
    "regions":regions,
    "region1":region1,
    'latest1':latest1,
    'latest6':latest6,
    'latestall':latestall,
    }
    return render(request,"category_news.html",context)

def region_news(request,slug):
    categorys=Category.objects.all()
    region1=Region.objects.all()[0]
    regions=Region.objects.all()[1:]
    region=Region.objects.get(slug=slug)
    latestall=News.objects.order_by("-created_at")[:5]
    latest=News.objects.filter(region=region).order_by("-created_at")[1:5]
    latest6=News.objects.filter(region=region).order_by("-created_at")[6:9]
    latest1=News.objects.filter(region=region).order_by("-created_at").first()
    context={
        "categorys":categorys,
        'region':region,
        'latest':latest,
        'latest6':latest6,
        'latest1':latest1,
        "regions":regions,
        "region1":region1,
        'latestall':latestall,
    }
    return render(request,"region.html",context)

def more_news(request,slug):
    categorys=Category.objects.all()
    region1=Region.objects.all()[0]
    regions=Region.objects.all()[1:]
    news11=News.objects.get(slug=slug)
    latest=News.objects.order_by("-created_at")[:5]
    count=News.objects.order_by("-views_count")[:5] 
    latestall=News.objects.order_by("-created_at")[:5]
    news11.views_count+=1
    news11.save()
    context={
        "categorys":categorys,
        'news11':news11,
        'latest':latest,
        "count":count,
        "regions":regions,
        "region1":region1,
        "latestall":latestall
        
    }
    return render(request,"more_news.html",context)