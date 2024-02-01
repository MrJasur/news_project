from urllib import request

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import News, Category
from .forms import ContactForm



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
    news = News.objects.all().order_by('-published_time')[:6]
    local_one = News.objects.all().filter(category__name='mahalliy').order_by("-published_time")[:1]
    local_news = News.objects.all().filter(category__name='mahalliy').order_by("-published_time")[1:6]
    foreign_news = News.objects.all().filter(category__name='xorij').order_by("-published_time")
    sport_news = News.objects.all().filter(category__name='sport').order_by("-published_time")
    technology_news = News.objects.all().filter(category__name='texnologiya').order_by("-published_time")
    categories = Category.objects.all()
    context = {'news': news,
               'categories': categories,
               'local_news': local_news,
               'local_one': local_one,
               'foreign_news': foreign_news,
               'sport_news': sport_news,
               'technology_news': technology_news}

    return render(request, 'news/index.html', context=context)


def contactPageView(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse("Thank you for contacting us")

    context = {'form': form}

    return render(request, 'news/contact.html', context=context)

def xatolikView(request):
    return render(request, 'news/404.html')

def seinglePageView(request, id):
    news_detail = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {'news': news_detail}
    return render(request, 'news/single_page.html', context=context)
