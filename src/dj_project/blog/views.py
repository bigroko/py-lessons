# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render
from blog.models import Blog


def index(request):
    blog_list = Blog.objects.order_by('-created')[:10]
    return render(request, 'index.html', {'blog_list': blog_list})


def detail(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog item does not exist")
    return render(request, 'detail.html', {'blog': blog})
