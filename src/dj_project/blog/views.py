# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render


def blog_viewset(request):
    return HttpResponse("blog")
