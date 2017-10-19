# coding:utf-8
from django.conf.urls import patterns, include, url
from cachemanage.views import *


urlpatterns = patterns('',
    url(r'^cachemanage_select/$', cachemanage_select, name='cachemanage_select'),
    url(r'^cachemanage_redislistjson/$', cachemanage_redislistjson, name='cachemanage_redislistjson'),
    url(r'^cachemanage_index/$', cachemanage_index, name='cachemanage_index'),

    url(r'^nginxdata/$', nginxdata, name='nginxdata'),
    url(r'^nginxmonitor/$', nginxmonitor, name='nginxmonitor'),
    url(r'^server_tree/$', server_tree, name='server_tree'),
    url(r'^overview/$', overview, name='overview'),






)