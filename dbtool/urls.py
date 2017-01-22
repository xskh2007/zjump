# coding:utf-8
from django.conf.urls import patterns, include, url
from dbtool.views import *


urlpatterns = patterns('',
    url(r'^$', index, name='dbtool'),
    url(r'^execute/$', dbtool_execute, name='dbtool_execute'),
    url(r'^myjson/$', dbtool_myjson, name='dbtool_myjson'),


)