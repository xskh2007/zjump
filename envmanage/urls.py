# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from envmanage.views import *



urlpatterns = patterns('',

    url(r'^envmanage_clone_index/$', envmanage_clone_index, name='envmanage_clone_index'),
    url(r'^envmanage_clone/$', envmanage_clone, name='envmanage_clone'),







)