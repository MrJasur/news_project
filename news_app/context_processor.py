from .models import News

def news_processor(request):
    latest_news = News.objects.all().order_by("-published_time")[:10]
    categories = News.objects.all()

    context = {
        "latest_news": latest_news,
        "categories": categories,
    }
    return context