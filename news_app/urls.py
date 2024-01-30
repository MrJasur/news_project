from django.urls import path
from .views import news_list, news_detail, homePageView, contactPageView, xatolikView, seinglePageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('contact/', contactPageView, name='contact'),
    path('404page/', xatolikView, name='404page'),
    path('singlepage/', seinglePageView, name='singlepage'),
    path('news/', news_list, name='news_list'),
    path('news_detail/<int:id>', news_detail, name='news_detail'),
]