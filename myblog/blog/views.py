from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

# def index(request):
#     #return  HttpResponse("hello,world!")
#     return  render(request,'blog/index.html',{'cwm':'chenwangming','age':28})

# def index(request):
#     article=models.Article.objects.get(pk=1)
#     return render(request,'blog/index.html',{'article':article})

def index(request):
    articles=models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})


def article_page(request,article_id):
    article=models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{"article":article})

def edit_page(requset,article_id):
    if(article_id=='0'):
        return  render(requset,'blog/edit_page.html')
    article=models.Article.objects.get(pk=article_id)
    return render(requset,'blog/edit_page.html',{'article':article})



def edit_action(request):
    title=request.POST.get('title','Title')
    content =request.POST.get('content','neirong')
    article_id=request.POST.get('id','0')
    if(article_id=='0'):
        models.Article.objects.create(tilte=title,content=content)
        articles=models.Article.objects.all()
        return render(request,'blog/index.html',{'articles':articles})
    article=models.Article.objects.get(pk=article_id)
    article.tilte=title
    article.content=content
    article.save()
    return render(request,'blog/article_page.html',{'article':article})