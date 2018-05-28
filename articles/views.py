from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

'''
Takes in the request object.
All we are going to do in this function is we will render a template
     to the user which is going to show a list of articles.
First parameter in render is always the request object and the second parameter is
     the template we want to render and third optional is the directory
'''
def articles_list(request):
    #Retrieve all articles from database and sort them according to date
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html',{'articles':articles})

def articles_details(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})

#if the user is not already logged in than send the user to login page first
@login_required(login_url="/accounts/login/")
def article_create(request):
    #if the request is post then retrieve the data,which user has entered in the form 
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', { 'form': form })