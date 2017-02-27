# -*- coding: utf-8 -*-
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from blog.models import Blog


@staff_member_required
def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'blog': blog})


def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    subject = request.POST['subject']
    text = request.POST['text']
    if subject == "" or text == "":
        return render(request, 'edit.html', {
            'blog': blog,
            'error_message': "You must fill all the fields.",
        })
    if len(subject) > 200:
        return render(request, 'edit.html', {
            'blog': blog,
            'error_message': "Subject must be 200 characters max.",
        })
    blog.subject = subject
    blog.text = text
    blog.save()
    return HttpResponseRedirect(reverse('index'))
