# coding:utf-8
from django.conf.urls import patterns, include, url
from cachemanage.views import *


urlpatterns = patterns('',
    url(r'^cachemanage_select/$', cachemanage_select, name='cachemanage_select'),
    url(r'^cachemanage_redislistjson/$', cachemanage_redislistjson, name='cachemanage_redislistjson'),






)