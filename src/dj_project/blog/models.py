# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return self.name


class Blog(models.Model):
    subject = models.CharField(max_length=200, verbose_name='Subject')
    text = models.TextField(verbose_name='Text')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name="User")
    tags = models.ManyToManyField(Tag, verbose_name='tags', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    updater = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="updater",
                                verbose_name="Updater")

    def tags_str(self):
        return ", ".join(map(str, self.tags.all().order_by("name")))

    def __str__(self):
        return "[ {}, {} ] {}".format(self.created,
                                      self.user,
                                      self.subject,)
