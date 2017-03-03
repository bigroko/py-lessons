# -*- coding: utf-8 -*-
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from blog.models import Blog

S = "subject"
T = "text"


@staff_member_required
def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'blog': blog})


def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    subject = request.POST[S].strip()
    text = request.POST[T].strip()

    val, err = __validate(blog, **{S: subject, T: text})
    if val:
        blog.subject = subject
        blog.text = text
        blog.updater = request.user
        blog.save()
    else:
        return render(request, "edit.html", {
            "blog": blog,
            "error_message": err
        })
    return HttpResponseRedirect(reverse("index"))


def __validate(blog, **kwargs):
    if kwargs[S] == "":
        return False, "Subject cannot be empty"
    if kwargs[T] == "":
        return False, "Text cannot be empty"
    if len(kwargs[S]) > 200:
        return False, "Subject must be 200 characters max"
    if blog.subject == kwargs[S] and blog.text == kwargs[T]:
        return False, "No changes were made"
    return True, ""
