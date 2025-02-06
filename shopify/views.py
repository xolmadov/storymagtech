from django.shortcuts import render, get_object_or_404
from .models import *

def popular_news(request):
    posts = Post.objects.all()
    first_post = posts.first()
    second_post = posts[1] if posts.count() > 1 else None
    gadgets = Gadget.objects.all().order_by('-created_at')
    news_list = News.objects.all().order_by('-created_at')[:6]
    latest_list = Latest.objects.all().order_by('-created_at')[:5]   # Eng oxirgi 6ta yangilikni chiqarish
    return render(request, 'shopify.html', {'news_list': news_list, 'gadgets': gadgets, 'latest_list': latest_list, "first_post": first_post, 
        "second_post": second_post, 
        "posts": posts})


def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'news_detail.html', {'news': news})

def gadget_detail(request, gadget_id):
    gadget = get_object_or_404(Gadget, id=gadget_id)
    return render(request, 'gadget_detail.html', {'gadget': gadget})

def lt_detail(request, latest_id):
    latest = get_object_or_404(Latest, id=latest_id)
    return render(request, 'lt_detail.html', {'latest': latest})



def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "trial.html", {"post": post})
