# -*- coding: utf-8 -*-
from django.views import generic
from blog.models import Blog


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        return Blog.objects.order_by('-created')[:10]


class DetailView(generic.DetailView):
    model = Blog
    template_name = 'detail.html'
