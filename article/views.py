# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from article.models import Article
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
# Create your views here.
def home(request):
    return HttpResponse("Hello World, Django")
def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s" 
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
#def test(request):
#    return render(request,'test.html',{'current_time':datetime.now()})
def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})
def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})
