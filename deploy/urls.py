# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from deploy.views import *



urlpatterns = patterns('',

    url(r'^deploy_all/$', deploy_all, name='deploy_all'),
    url(r'^deploy_increment/$', deploy_increment, name='deploy_increment'),








)