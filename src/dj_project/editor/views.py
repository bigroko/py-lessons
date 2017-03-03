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
    subject = request.POST["subject"].strip()
    text = request.POST["text"].strip()

    val, err = __validate(blog, **{
        "subject": subject,
        "text": text
    })
    if val:
        blog.subject = subject
        blog.text = text
        blog.save()
    else:
        return render(request, "edit.html", {
            "blog": blog,
            "error_message": err
        })
    return HttpResponseRedirect(reverse("index"))


def __validate(blog, **kwargs):
    if kwargs["subject"] == "":
        return False, "Subject cannot be empty"
    if kwargs["text"] == "":
        return False, "Text cannot be empty"
    if len(kwargs["subject"]) > 200:
        return False, "Subject must be 200 characters max"
    if blog.subject == kwargs["subject"] and blog.text == kwargs["text"]:
        return False, "No changes were made"
    return True, ""
