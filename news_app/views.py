from urllib import request

from django.shortcuts import render, get_object_or_404
from .models import News, Category
# Create your views here.
def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)
    context = {'news_list': news_list}
    return render(request, 'news/news_list.html', context=context)


def news_detail(request, id):
    news_detail = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {'news_detail': news_detail}
    return render(request, 'news/news_detail.html', context=context)

def homePageView(request):
    news = News.objects.filter(status=News.Status.Published)
    categories = Category.objects.all()
    context = {'news': news, 'categories': categories}

    return render(request, 'news/index.html', context=context)


def contactPageView(request):
    return render(request, 'news/contact.html')

def xatolikView(request):
    return render(request, 'news/404.html')

def seinglePageView(request):
    return render(request, 'news/single_page.html')
