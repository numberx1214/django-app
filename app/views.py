from django.shortcuts import render
from .models import News, Blog


# Create your views here.
def base(request):
    return render(request, 'base.html')


def news(request):
    old = News.objects.filter(id=3).update(title="this title has changed because id was 3 :)")
    news = News.objects.all().order_by('-publish')
    context = {
        "title": "news page",
        "news": news
    }
    return render(request, 'news.html', context=context)


def blog(request):
    old=Blog.objects.filter(name="newwwwww")
    for older in old:

        new=Blog.objects.create(name="new2", content=f"this content created because blog object {older.name} have been deleted")
    old.delete()
    blog = Blog.objects.all().order_by('-id')[:4]
    context = {
        "title": "blog page",
        "blog": blog
    }
    return render(request, 'blog.html', context)
