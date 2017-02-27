# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Blog, Tag


admin.site.register(Tag)
admin.site.register(Blog)
